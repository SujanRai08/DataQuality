### Weather Data Automation and Monitoring

### *overview*
This project automates the process of fetching weather data from the OpenWeatherMap API at regular intervals, stores the data in a CSV file, and can be used for analysis or further data cleaning tasks. It provides a foundation for data collection and monitoring, useful for data engineering and data science applications.

### *Features*
- Fetches weather data (temperature, humidity, wind speed, rainfall) from the OpenWeatherMap API.
- Saves collected data into a CSV file (weather_data.csv).
- Automation: Data is fetched every hour (or customizable interval) until a set number of data points (10 in this version).
  
### *Set up*
1. Install required packages:
```python
pip install requests pandas python-dotenv
```
2. Set up API key:
   - create an account at OpenWeatherMap and get an API key.
   - store your API key in .env file:
    ```makefile
    WEATHER_API_KEY=your api key 
    ```
3. Run the Scipt:
   - The script fetches weather data and appends it to weather_data.csv.
   - Data collection stops after 10 data points (configurable).

4. Customization:
   - Change the location by modifying the q parameter in the API request.
   - Adjust the interval and data collection limit as needed.

### *Future updates*
- Add support for different data storage solutions (e.g., PostgreSQL).
- Expand the project to include data cleaning and anomaly detection.
- Automate data visualization and reporting for insights.
