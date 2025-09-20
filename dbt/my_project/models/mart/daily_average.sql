{{config(
    materialized='table'
)}}

SELECT 
    city,
    DATE(local_time) AS date,
    ROUND(AVG(temperature::NUMERIC),2) AS avg_temp,
    ROUND(AVG(wind_speed::NUMERIC),2) AS avg_windspeed
FROM {{ref('stg_weather_data')}}
GROUP BY 1,2
ORDER BY 1,2