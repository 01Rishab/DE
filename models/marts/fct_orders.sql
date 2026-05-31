with orders as (
    select * from {{ ref('stg_orders') }}
),

customers as (
    select * from {{ ref('stg_customers') }}
),

products as (
    select * from {{ ref('stg_products') }}
),

final as (
    select
        o.order_id,
        o.order_date,
        o.status,
        o.quantity,

        c.customer_id,
        c.customer_name,
        c.city,

        p.product_id,
        p.product_name,
        p.category,
        p.price,

        round(o.quantity * p.price, 2)  as total_amount
    from orders o
    left join customers c on o.customer_id = c.customer_id
    left join products p on o.product_id = p.product_id
)

select * from final