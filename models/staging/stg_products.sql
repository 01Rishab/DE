with source as (
    select * from raw.products
),

renamed as (
    select
        product_id,
        name                            as product_name,
        category,
        price
    from source
)

select * from renamed