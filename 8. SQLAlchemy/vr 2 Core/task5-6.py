from task import Employees, Clients, Suppliers, Deliveries, Products, Orders, engine
from sqlalchemy import select

# Получение и вывод данных из таблицы Employees
with engine.begin() as conn:
    stmt = select(Employees)
    employees = conn.execute(stmt).fetchall()
    print("----- Employees -----")
    for employee in employees:
        print(employee)

# Получение и вывод данных из таблицы Clients
with engine.begin() as conn:
    stmt = select(Clients)
    clients = conn.execute(stmt).fetchall()
    print("\n----- Clients -----")
    for client in clients:
        print(client)

# Получение и вывод данных из таблицы Suppliers
with engine.begin() as conn:
    stmt = select(Suppliers)
    suppliers = conn.execute(stmt).fetchall()
    print("\n----- Suppliers -----")
    for supplier in suppliers:
        print(supplier)

# Получение и вывод данных из таблицы Deliveries
with engine.begin() as conn:
    stmt = select(Deliveries)
    deliveries = conn.execute(stmt).fetchall()
    print("\n----- Deliveries -----")
    for delivery in deliveries:
        print(delivery)

# Получение и вывод данных из таблицы Products
with engine.begin() as conn:
    stmt = select(Products)
    products = conn.execute(stmt).fetchall()
    print("\n----- Products -----")
    for product in products:
        print(product)

# Получение и вывод данных из таблицы Orders
with engine.begin() as conn:
    stmt = select(Orders)
    orders = conn.execute(stmt).fetchall()
    print("\n----- Orders -----")
    for order in orders:
        print(order)

# Inner Join: Employees and Orders
with engine.begin() as conn:
    stmt = select(Employees, Orders).join(Orders, Employees.c.EmployeeID == Orders.c.EmployeeID)
    join_result = conn.execute(stmt).fetchall()
    print("\n----- Employees and Orders -----")
    for row in join_result:
        print(row)

# Inner Join: Suppliers and Deliveries
with engine.begin() as conn:
    stmt = select(Suppliers, Deliveries).join(Deliveries, Suppliers.c.SupplierID == Deliveries.c.SupplierID)
    join_result = conn.execute(stmt).fetchall()
    print("\n----- Suppliers and Deliveries -----")
    for row in join_result:
        print(row)

# Inner Join: Products and Orders
with engine.begin() as conn:
    stmt = select(Products, Orders).join(Orders, Products.c.ProductID == Orders.c.ProductID)
    join_result = conn.execute(stmt).fetchall()
    print("\n----- Products and Orders -----")
    for row in join_result:
        print(row)

# Inner Join: Clients and Orders
with engine.begin() as conn:
    stmt = select(Clients, Orders).join(Orders, Clients.c.ClientID == Orders.c.ClientID)
    join_result = conn.execute(stmt).fetchall()
    print("\n----- Clients and Orders -----")
    for row in join_result:
        print(row)