-- Import
WITH source AS (
    SELECT
        "Date",
        "Close",
        "toten"
    FROM {{ source("dbcommodities", "commodities") }}
),

-- Renamed and converted
renamed AS (
    SELECT
       cast("Date" as date) as date,  -- Convert to date
       "Close" as close_price,
       "toten" as ticker
    from source
)

SELECT * FROM renamed