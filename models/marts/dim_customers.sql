with customers as (
    select * from {{ ref('stg_customers') }}
),

orders as (
    select * from {{ ref('stg_orders') }}
),

customer_stats as (
    select
        customer_id,
        count(order_id)                             as total_orders,
        count(case when status = 'completed'
                   then 1 end)                      as completed_orders,
        count(case when status = 'cancelled'
                   then 1 end)                      as cancelled_orders,
        min(order_date)                             as first_order_date,
        max(order_date)                             as last_order_date
    from orders
    group by customer_id
),

final as (
    select
        c.customer_id,
        c.customer_name,
        c.email,
        c.city,
        c.signup_date,
        coalesce(s.total_orders, 0)                 as total_orders,
        coalesce(s.completed_orders, 0)             as completed_orders,
        coalesce(s.cancelled_orders, 0)             as cancelled_orders,
        s.first_order_date,
        s.last_order_date
    from customers c
    left join customer_stats s on c.customer_id = s.customer_id
)

select * from final