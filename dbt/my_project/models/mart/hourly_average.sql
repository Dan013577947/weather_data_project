{{config(
    materialized='table'
)}}

SELECT
    house_number,
    street,
    barangay,
    city, 
    EXTRACT(HOUR FROM local_time) AS hour,
    ROUND(AVG(temperature::NUMERIC),2) AS avg_temp,
    ROUND(AVG(wind_speed::NUMERIC),2) AS avg_windspeed
FROM {{ref('stg_weather_data')}}
GROUP BY 1,2,3,4,5
ORDER BY 6 DESC,7 DESC
