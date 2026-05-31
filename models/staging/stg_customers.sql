with source as (
    select * from raw.customers
),

renamed as (
    select
        customer_id,
        name                            as customer_name,
        email,
        city,
        cast(signup_date as date)       as signup_date
    from source
)

select * from renamed