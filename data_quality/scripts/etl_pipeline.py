import os
import time
import logging
import pandas as pd
import requests
from dotenv import load_dotenv
from psycopg2 import connect, sql, OperationalError

# Configure logging
logging.basicConfig(
    filename='etl_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables
load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')

# API and database configuration
base_url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Kathmandu", "appid": api_key, "units": "metric"}

db_config = {
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "database": os.getenv("POSTGRES_DB"),
}

data_limit = 10  # Number of records to fetch
interval = 3600  # Fetch interval in seconds

# Function to connect to PostgreSQL
def connect_to_db():
    try:
        conn = connect(**db_config)
        logging.info("Connected to the PostgreSQL database successfully.")
        return conn
    except OperationalError as e:
        logging.error(f"Database connection failed: {e}")
        raise

# Main ETL function
def fetch_and_store_weather_data():
    record_count = 0
    conn = connect_to_db()

    while record_count < data_limit:
        try:
            # Extract
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                logging.info("Successfully fetched weather data.")
            else:
                logging.error(f"API error {response.status_code}: {response.text}")
                continue

            # Transform
            weather_data = {
                "date": pd.Timestamp.now(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "rainfall": data.get("rain", {}).get("1h", 0),
            }
            logging.info(f"Transformed weather data: {weather_data}")

            # Load into CSV
            df = pd.DataFrame([weather_data])
            df.to_csv("data/weather_data.csv", mode="a", index=False, header=False)
            logging.info("Data appended to CSV file.")

            # Load into PostgreSQL
            with conn.cursor() as cur:
                insert_query = sql.SQL("""
                    INSERT INTO weather (date, temperature, humidity, wind_speed, rainfall)
                    VALUES (%s, %s, %s, %s, %s)
                """)
                cur.execute(insert_query, tuple(weather_data.values()))
                conn.commit()
                logging.info("Data inserted into PostgreSQL database.")

            record_count += 1
        except Exception as e:
            logging.error(f"An error occurred: {e}")

        # Wait for the next interval
        time.sleep(interval)

    conn.close()
    logging.info("ETL pipeline completed. Exiting script.")

if __name__ == "__main__":
    logging.info("Starting ETL pipeline...")
    fetch_and_store_weather_data()
    logging.info("ETL pipeline terminated.")
