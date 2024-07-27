import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import  seaborn as sns
import plotly.figure_factory as ff
from plotly.figure_factory import create_distplot
import preprocessor, helper

# load data
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df = preprocessor.preprocess(df,region_df)

# ----------- Olympic Analysis ----------- #
st.sidebar.title('Olympics Analysis')
st.sidebar.image('https://th.bing.com/th/id/OIP.PvpbNcO0Qif5hHQvpfL4SgAAAA?rs=1&pid=ImgDetMain')
user_menu = st.sidebar.radio(
    'Select an Option: ',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

# st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox('Select Year: ', years)
    selected_country = st.sidebar.selectbox('Select Country: ', country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Tally')
    if selected_year != 'Overall ' and selected_country == 'Overall':
        st.title('Medal Tally in  ' + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performace in " + str(selected_year) + " Olympics")
    st.table(medal_tally)


if user_menu == 'Overall Analysis':
    st.sidebar.header('Overall Analysis')

    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title('Top Statistics')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nations)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x='Editions', y='region')
    st.title('Participating Nations Over the Years')
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Editions', y='Event')
    st.title('Events Over the Years')
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x='Editions', y='Name')
    st.title('Athletes Over the Years')
    st.plotly_chart(fig)

    st.title('No of Events over time (Every Sports)')
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int')
                , annot=True)
    st.pyplot(fig)

    st.title('Most Sucessful Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x: object = helper.most_sucessful(df,selected_sport)
    st.table(x)


if user_menu == 'Country-wise Analysis':
    st.sidebar.header('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select a Country', country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(selected_country + ' Medal Tally over the years ')
    st.plotly_chart(fig)


    st.title(selected_country + ' execel in the following sports')

    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title('To 10 Athletes of '+ selected_country)
    top10_df = helper.most_sucessful_countrywise(df,selected_country)
    st.table(top10_df)


if user_menu == 'Athlete wise Analysis':
    athletes_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athletes_df['Age'].dropna()
    x2 = athletes_df[athletes_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athletes_df[athletes_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athletes_df[athletes_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height = 600)
    st.title('Distriution of Age')
    st.plotly_chart(fig)


    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(data=temp_df, x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'],
                    s=60)
    st.pyplot(fig)


    st.title('Men Vs Women Participation Over the Years')
    final = helper.men_v_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height = 600)
    st.plotly_chart(fig)