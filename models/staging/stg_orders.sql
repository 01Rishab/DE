with source as (
    select * from raw.orders
),

renamed as (
    select
        order_id,
        customer_id,
        product_id,
        quantity,
        status,
        cast(order_date as date)        as order_date
    from source
)

select * from renamed