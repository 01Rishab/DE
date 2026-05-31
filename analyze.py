import duckdb

con = duckdb.connect("ecommerce.duckdb")

print("\n📦 TOP 5 CITIES BY REVENUE")
print(con.execute("""
    select city, round(sum(total_amount), 2) as revenue
    from main_marts.fct_orders
    where status = 'completed'
    group by city
    order by revenue desc
    limit 5
""").df().to_string(index=False))

print("\n🛍️ TOP 5 PRODUCT CATEGORIES BY ORDERS")
print(con.execute("""
    select category, count(*) as total_orders
    from main_marts.fct_orders
    group by category
    order by total_orders desc
    limit 5
""").df().to_string(index=False))

print("\n👤 TOP 5 CUSTOMERS BY SPENDING")
print(con.execute("""
    select customer_name, city, round(sum(total_amount), 2) as total_spent
    from main_marts.fct_orders
    where status = 'completed'
    group by customer_name, city
    order by total_spent desc
    limit 5
""").df().to_string(index=False))

con.close()