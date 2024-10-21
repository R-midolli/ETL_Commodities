-- Import
WITH source AS (
    SELECT
        "Date",
        "Close",
        "toten"
    FROM {{ source("dbcommodities", "commodities") }}
),

-- Renamed
renamed AS (
    SELECT
       cast("Date" as timestamp) as date,
       "Close" as close_price,
       "toten" as ticker
    from source
)

SELECT * FROM renamed
