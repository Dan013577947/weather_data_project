{{config(
    materialized='table',
    unique_key='id'
)}}

WITH source AS(
    SELECT * FROM {{source('dev','raw_weather_data')}}
),
remove_duplicates AS(
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY DATE(local_time), CAST(local_time AS TIME) ORDER BY inserted_at DESC) AS rnk
    FROM source
)
SELECT 
    id,
    city,
    local_time,
    temperature,
    wind_speed,
    weather_descriptions,
    (inserted_at + (utc_offset||'hours')::INTERVAL) AS inserted_at_local
FROM remove_duplicates
WHERE rnk=1
