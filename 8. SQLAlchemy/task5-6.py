from task import Employee, Client, Supplier, Delivery, Product, Order, Session, engine
from sqlalchemy.orm import sessionmaker

'''5. Получите данные из таблицы и выведите на экран.'''
session = Session()

# Получение и вывод данных из таблицы Employees
employees = session.query(Employee).all()
print("----- Employees -----")
for employee in employees:
    print(
        f"EmployeeID: {employee.EmployeeID}, LastName: {employee.LastName}, FirstName: {employee.FirstName}, MiddleName: {employee.MiddleName}, Position: {employee.Position}, Address: {employee.Address}, HomePhone: {employee.HomePhone}, BirthDate: {employee.BirthDate}")

# Получение и вывод данных из таблицы Clients
clients = session.query(Client).all()
print("\n----- Clients -----")
for client in clients:
    print(f"ClientID: {client.ClientID}, FullName: {client.FullName}, Address: {client.Address}, Phone: {client.Phone}")

# Получение и вывод данных из таблицы Suppliers
suppliers = session.query(Supplier).all()
print("\n----- Suppliers -----")
for supplier in suppliers:
    print(
        f"SupplierID: {supplier.SupplierID}, SupplierName: {supplier.SupplierName}, SupplierRepresentative: {supplier.SupplierRepresentative}, ContactPhone: {supplier.ContactPhone}, Address: {supplier.Address}")

# Получение и вывод данных из таблицы Deliveries
deliveries = session.query(Delivery).all()
print("\n----- Deliveries -----")
for delivery in deliveries:
    print(
        f"DeliveryID: {delivery.DeliveryID}, SupplierID: {delivery.SupplierID}, DeliveryDate: {delivery.DeliveryDate}")

# Получение и вывод данных из таблицы Products
products = session.query(Product).all()
print("\n----- Products -----")
for product in products:
    print(
        f"ProductID: {product.ProductID}, DeliveryID: {product.DeliveryID}, ProductName: {product.ProductName}, TechnicalSpecifications: {product.TechnicalSpecifications}, Description: {product.Description}, Image: {product.Image}, PurchasePrice: {product.PurchasePrice}, SalePrice: {product.SalePrice}")

# Получение и вывод данных из таблицы Orders
orders = session.query(Order).all()
print("\n----- Orders -----")
for order in orders:
    print(
        f"OrderID: {order.OrderID}, EmployeeID: {order.EmployeeID}, ProductID: {order.ProductID}, OrderDate: {order.OrderDate}, ExecutionDate: {order.ExecutionDate}, ClientID: {order.ClientID}")

# Закрытие сессии
session.close()

'''6. Сделайте несколько Inner join запросов и выведите на экран результат.'''

# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Inner Join: Employees and Orders
print("----- Employees and Orders -----")
join_result = session.query(Employee, Order).join(Order, Employee.EmployeeID == Order.EmployeeID).all()
for employee, order in join_result:
    print(
        f"EmployeeID: {employee.EmployeeID}, LastName: {employee.LastName}, FirstName: {employee.FirstName}, OrderID: {order.OrderID}, OrderDate: {order.OrderDate}, ExecutionDate: {order.ExecutionDate}")

# Inner Join: Suppliers and Deliveries
print("\n----- Suppliers and Deliveries -----")
join_result = session.query(Supplier, Delivery).join(Delivery, Supplier.SupplierID == Delivery.SupplierID).all()
for supplier, delivery in join_result:
    print(
        f"SupplierID: {supplier.SupplierID}, SupplierName: {supplier.SupplierName}, SupplierRepresentative: {supplier.SupplierRepresentative}, DeliveryID: {delivery.DeliveryID}, DeliveryDate: {delivery.DeliveryDate}")

# Inner Join: Products and Orders
print("\n----- Products and Orders -----")
join_result = session.query(Product, Order).join(Order, Product.ProductID == Order.ProductID).all()
for product, order in join_result:
    print(
        f"ProductID: {product.ProductID}, ProductName: {product.ProductName}, OrderID: {order.OrderID}, OrderDate: {order.OrderDate}, ExecutionDate: {order.ExecutionDate}")

# Inner Join: Clients and Orders
print("\n----- Clients and Orders -----")
join_result = session.query(Client, Order).join(Order, Client.ClientID == Order.ClientID).all()
for client, order in join_result:
    print(
        f"ClientID: {client.ClientID}, FullName: {client.FullName}, OrderID: {order.OrderID}, OrderDate: {order.OrderDate}, ExecutionDate: {order.ExecutionDate}")

# Закрытие сессии
session.close()
