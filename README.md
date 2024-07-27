# Olympic Analysis Project

## Overview

This project analyzes 120 years of Olympic history, focusing on athletes and results. The analysis includes medal tallies, overall statistics, country-wise analysis, and athlete-wise analysis. The project also includes a Streamlit web app for interactive exploration of the data.

## Data Sources

- **Athlete Events:** [Kaggle Dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- **NOC Regions:** [Kaggle Dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

## Project Structure

```
.
├── app.py
├── preprocessor.py
├── helper.py
├── athlete_events.csv
├── noc_regions.csv
└── requirements.txt
```

## Files Description

### app.py

The main script for the Streamlit web application. It allows users to explore various aspects of the Olympic data through interactive visualizations and tables.

### preprocessor.py

Contains functions to preprocess the data, including filtering for Summer Olympics, merging with region data, dropping duplicates, and encoding medal columns.

### helper.py

Includes helper functions for generating specific analysis and visualizations, such as medal tally, country-wise analysis, athlete-wise analysis, and more.

### athlete_events.csv

The primary dataset containing information about athletes and their performance in various Olympic events.

### noc_regions.csv

Dataset containing information about the National Olympic Committees (NOCs) and their corresponding regions.

### requirements.txt

A list of Python packages required to run the project.

## Installation

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/olympic-analysis.git
cd olympic-analysis
```

2. **Create a virtual environment:**

```sh
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

3. **Install the dependencies:**

```sh
pip install -r requirements.txt
```

4. **Run the Streamlit app:**

```sh
streamlit run app.py
```

## Usage

1. **Medal Tally:**
   - View the overall or specific year/country medal tally.

2. **Overall Analysis:**
   - Explore top statistics like the number of editions, cities, sports, events, athletes, and nations.
   - View the number of participating nations, events, and athletes over the years.
   - See a heatmap of the number of events over time for each sport.
   - View the most successful athletes in each sport.

3. **Country-wise Analysis:**
   - Explore the medal tally of a selected country over the years.
   - View a heatmap of the country's performance in different sports.
   - See the top 10 athletes of the selected country.

4. **Athlete-wise Analysis:**
   - View the age distribution of athletes who have won medals.
   - Explore the height vs. weight distribution for athletes in different sports.
   - Analyze the participation of men and women over the years.

## Sample Visualizations

![Medal Tally](images/medal_tally.png)
![Overall Analysis](images/overall_analysis.png)
![Country-wise Analysis](images/country_analysis.png)
![Athlete-wise Analysis](images/athlete_analysis.png)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
