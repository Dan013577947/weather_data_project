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
    utc_offset FLOAT);

CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE airflow_db OWNER airflow;