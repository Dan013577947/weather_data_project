{{config(
    materialized='table'
)}}


WITH source AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY DATE(local_time) ORDER BY temperature DESC, wind_speed DESC) AS rnk
    FROM {{ref('stg_weather_data')}}
)
SELECT
    DATE(local_time) AS date,
    CAST(local_time AS TIME) AS time,
    house_number,
    street,
    barangay,
    city,
    temperature,
    wind_speed
FROM source
WHERE rnk = 1
ORDER BY 1 DESC,2 DESC



