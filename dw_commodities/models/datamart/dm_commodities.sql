-- models/datamart/dm_commodities.sql

with commodities as (
    select
        date,
        ticker,
        close_price
    from 
        {{ ref ('stg_commodities') }}
),

transactions as (
    select
        date,
        ticker,
        transaction_type,
        quantity
    from 
        {{ ref ('stg_commodities_transactions') }}
),

joined as (
    select
        c.date,
        c.ticker,
        c.close_price,
        t.transaction_type,
        t.quantity,
        (t.quantity * c.close_price) as value,
        case
            when t.transaction_type = 'sell' then (t.quantity * c.close_price)
            else -(t.quantity * c.close_price)
        end as profit_loss
    from
        commodities c
    inner join
        transactions t
    on
        c.date = t.date
        and c.ticker = t.ticker
),

last_day as (
    select
        max(date) as max_date
    from
        joined
),

filtered as (
    select
        *
    from
        joined
    where
        date = (select max_date from last_day)
)

select
    date,
    ticker,
    close_price,
    transaction_type ,
    quantity,
    value,
    profit_loss
from
    filtered
