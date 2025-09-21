from api_request import mock_fetch_data
from api_request import fetch_data
import psycopg2

def connect_db():
    print("Connecting to database on process..")
    try:
        conn = psycopg2.connect(
            host='db',
            port=5432,
            dbname='db',
            user='db_user',
            password='db_password'
        )
        conn.commit()
        print("Connecting to database successful")
        return conn
    except psycopg2.Error as e:
        print(f"Error occured while connecting to database: {e}")
        raise

def create_table(conn):
    print("Creating table on process..")
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
                id SERIAL PRIMARY KEY,
                house_number INT,
                street VARCHAR(25),
                barangay VARCHAR(20),
                city VARCHAR(20),
                local_time TIMESTAMP,
                temperature FLOAT,
                wind_speed FLOAT,
                weather_descriptions TEXT, 
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset FLOAT
            )
            """
        )
        conn.commit()
        print("Creating table successful")
        return conn
    except psycopg2.Error as e:
        print(f"Error occured while creating table: {e}")
        raise


def insert_table(conn ,data):
    print("Inserting data to table on process..")
    try:
        current = data['current']
        location = data['location']

        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO dev.raw_weather_data(
                house_number,
                street,
                barangay,
                city,
                local_time,
                temperature,
                wind_speed,
                weather_descriptions,
                inserted_at,
                utc_offset
            ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s);
            """,(
                '193',
                'Cadena de amor street',
                'Bahay Toro',
                'Quezon City',
                location['localtime'],
                current['temperature'],
                current['wind_speed'],
                current['weather_descriptions'],
                location['utc_offset']
            )
        )
        conn.commit()
        print("Inserting data to table successful")
        return conn
    except psycopg2.Error as e:
        print(f"Error occured while inserting data to table: {e}")
        raise

def main():
    try:
        conn = connect_db()
        data = fetch_data()
        # data = mock_fetch_data()
        create_table(conn)
        insert_table(conn, data)
    except Exception as e:
        print(f"Error while in main: {e}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed")

