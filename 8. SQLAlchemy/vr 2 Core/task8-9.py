from task import Employees, Clients, Products, Orders, engine
from sqlalchemy import select, func, distinct

'''8. Получите данные вместе с WHERE, ORDER BY, GROUP BY, DISTINCT и выведите на экран.'''

# Запросы с WHERE, ORDER BY, GROUP BY, DISTINCT
print("----- Запрос с WHERE -----")
with engine.begin() as conn:
    result = conn.execute(select(Employees).where(Employees.c.LastName == 'Иванов')).all()

    for row in result:
        print(row)

print("\n----- Запрос с ORDER BY -----")
with engine.begin() as conn:
    result = conn.execute(select(Employees).order_by(Employees.c.BirthDate))

    for row in result:
        print(row)

print("\n----- Запрос с GROUP BY -----")
with engine.begin() as conn:
    result = conn.execute(
        select(
            func.substring(Clients.c.Address, 4, 7).label('City'),
            func.count('*').label('Count')
        ).group_by('City')
    ).all()

    for row in result:
        print(row)

print("\n----- Запрос с DISTINCT -----")
with engine.begin() as conn:
    result = conn.execute(
        select(
            distinct(Employees.c.Position)
        )
    ).all()

    for row in result:
        print(row)


'''9. Примените несколько функций агрегации и выведите результат на экран'''

# Применение функций агрегации
print("----- Функции агрегации -----")

# Средняя цена продажи товаров
with engine.begin() as conn:
    stmt = select(func.avg(Products.c.SalePrice))
    average_sale_price = conn.execute(stmt).scalar()
    print(f"Средняя цена продажи товаров: {average_sale_price}")

# Количество заказов за определенный период
with engine.begin() as conn:
    stmt = select(func.count(Orders.c.OrderID)).where(Orders.c.OrderDate >= '2023-12-01')
    orders_count = conn.execute(stmt).scalar()
    print(f"Количество заказов с 2023-12-01: {orders_count}")

# Максимальная цена покупки
with engine.begin() as conn:
    stmt = select(func.max(Products.c.PurchasePrice))
    max_purchase_price = conn.execute(stmt).scalar()
    print(f"Максимальная цена покупки: {max_purchase_price}")