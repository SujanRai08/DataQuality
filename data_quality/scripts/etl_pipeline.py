import pandas as pd
import os
import requests
import pandas as pd
import psycopg2
import time 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "Kathmandu"

DB_SETTINGS ={
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

def fetch_weather_data():
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL,params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "date": pd.Timestamp.now(),
            "temperature":data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "rainfall": data.get("rain", {}).get("1h", 0),
        }
        return weather_data
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def save_csv(weather_data,file_path ="data/weather_data.csv"):
    df = pd.DataFrame([weather_data])
    df.to_csv(file_path,mode="a",index=False,header=not os.path.exists(file_path))
    print(f"Data saved to {file_path}")


def save_to_postgres(weather_data):
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            date TIMESTAMP,
            temperature FLOAT,
            humidity INT,
            wind_speed FLOAT,
            rainfall FLOAT
        )
        """)
        cursor.execute("""
        INSERT INTO weather_data (date, temperature, humidity, wind_speed, rainfall)
        VALUES (%s, %s, %s, %s, %s)
        """, (weather_data["date"], weather_data["temperature"],
              weather_data["humidity"], weather_data["wind_speed"],
              weather_data["rainfall"]))
        conn.commit()
        print("Data saved to PostgreSQL")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error saving to PostgreSQL:", e)


def etl_pipeline(interval=3600,max_iteration=10):
    iteration = 0
    while iteration < max_iteration:
        print(f"fetching data (iteration{iteration +1 }/ {max_iteration})")
        weather_data = fetch_weather_data()
        if weather_data:
            save_csv(weather_data)
            save_to_postgres(weather_data)
        iteration += 1
        if iteration < max_iteration:
            time.sleep(interval)

if __name__ == "__main__":
    etl_pipeline(interval=3600, max_iterations=10)

