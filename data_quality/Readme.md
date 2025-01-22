# Weather Data Automation and Monitoring

## Overview
This project automates the process of fetching weather data from the OpenWeatherMap API at regular intervals. It stores the data in a CSV file (`weather_data.csv`) and lays the groundwork for data analysis or further data cleaning tasks. Designed as a foundational tool for data engineering and data science applications, this project demonstrates the use of API integration and ETL automation.

## Features
- Fetches weather data (temperature, humidity, wind speed, rainfall) from the OpenWeatherMap API.
- Saves collected data into a CSV file (`weather_data.csv`).
- Automation: Fetches data every hour (or customizable interval) until a set number of data points (10 in this version).

## Setup
### 1. Install Required Packages:
```bash
pip install requests pandas python-dotenv
```
### 2. Set up API key:
- create an account at OpenWeatherMap and abtain an API key.
- Store your API key in a .env file:

```makefile
WEATHER_API_KEY=your_api_key
```

### 3. PostgreSQL Database configuration
- install PostgreSQL on your system(if not installed)
- create a database named weather_data:
```sql
CREATE DATABASE weather_data;
```
- Create a table to store weather data:
```sql
CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    temperature FLOAT NOT NULL,
    humidity INT NOT NULL,
    wind_speed FLOAT NOT NULL,
    rainfall FLOAT DEFAULT 0
);

```
- Add PostgreSQL connection details in the .env file.
```sql
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=weather_data
```

##  Running the Project
1. Automated Data Collection Script
   running the python scripts to fetch and store weather data.
   ```bash
   python scripts/etl_pipeline.py
   ```
2. Functionality
- CSV File Storage: The script appends data to weather_data.csv for flat-file storage.
- PostgreSQL Integration: Each fetched data point is inserted into the weather table in the database.


## Code Workflow
### ETL process
1. Extract:
   - Fetch weather data from the OpenWeatherMap API using Python's requests module.
2. Transform:
   - Extract relevant fields (temperature, humidity, wind speed, rainfall) and timestamp the data.
3. Load: 
   - Append the data to a CSV file.
   - Insert the data into a PostgreSQL table.
4. Automation:
   - A loop fetches data every hour (default interval) until the specified data limit is reached. This can be customized for different use cases.

## Customization
1. API Location:
- Change the q parameter in the API request to fetch data for a different city (e.g., New York or London).
2. Interval:
- Modify the time.sleep value in the script to adjust the data collection frequency.
3. Data Limit:
- Set the data_limit variable to determine how many data points to collect in a session.



## Future Enhancements
- Add data cleaning and anomaly detection steps.
- Integrate data visualization and dashboards using tools like Plotly or Tableau.
- Expand to multiple locations using dynamic API calls.
- Implement cloud-based storage solutions for scalability (e.g., AWS S3 or Google BigQuery).


This project is designed to help you gain hands-on experience with API integration, ETL pipelines, PostgreSQL, and data automation. Feel free to expand upon this foundation for your specific use cases.
```vbnet
# structure of the project folder
project/ │ ├── data/ │ ├── weather_data.csv │ ├── scripts/ │ ├── etl_pipeline.py │ ├── .env ├── .gitignore ├── README.md └── requirements.txt
```