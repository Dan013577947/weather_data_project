{{config(
    materialized='table'
)}}

SELECT
    house_number,
    street,
    barangay,
    city, 
    EXTRACT(YEAR FROM local_time) AS year,
    EXTRACT(MONTH FROM local_time) AS month,
    ROUND(AVG(temperature::NUMERIC),2) AS avg_temp,
    ROUND(AVG(wind_speed::NUMERIC),2) AS avg_windspeed
FROM {{ref('stg_weather_data')}}
GROUP BY 1,2,3,4,5,6
ORDER BY 5 DESC,6 DESC
