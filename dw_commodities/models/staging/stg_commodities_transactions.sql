--models/staging/stg_commodities.transactions.sql

with source as (
    SELECT
        date,
        symbol,
        action,
        quantity
    FROM {{ source("dbcommodities", "commodities_transactions") }}
),

renamed as (
    SELECT
        cast(date as date) as date,
        symbol as ticker,
        action as transaction_type,
        quantity as quantity
    from source
)

select * from renamed