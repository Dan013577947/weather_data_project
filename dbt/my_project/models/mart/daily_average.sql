{{config(
    materialized='table'
)}}

SELECT 
    house_number,
    street,
    barangay,
    city,
    DATE(local_time) AS date,
    ROUND(AVG(temperature::NUMERIC),2) AS avg_temp,
    ROUND(AVG(wind_speed::NUMERIC),2) AS avg_windspeed
FROM {{ref('stg_weather_data')}}
GROUP BY 1,2,3,4,5
ORDER BY 5 DESC