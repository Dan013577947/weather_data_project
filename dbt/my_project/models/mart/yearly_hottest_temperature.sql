
{{config(
    materialized='table'
)}}


WITH source AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY EXTRACT(YEAR FROM local_time) ORDER BY temperature DESC) AS rnk
    FROM {{ref('stg_weather_data')}}
)
SELECT
    EXTRACT(YEAR FROM local_time) AS year,
    EXTRACT(MONTH FROM local_time) AS month,
    EXTRACT(DAY FROM local_time) AS day,
    house_number,
    street,
    barangay,
    city,
    temperature,
    wind_speed
FROM source
WHERE rnk = 1
ORDER BY 1 DESC




