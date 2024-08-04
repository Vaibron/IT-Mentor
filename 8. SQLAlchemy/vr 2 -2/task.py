from sqlalchemy import create_engine, Table, Column, Integer, String, Date, Text, Numeric, ForeignKey, MetaData


engine = create_engine('postgresql://postgres:5981@localhost:5432/new_db', echo=True)

metadata = MetaData()

# Таблица Employees
Employees = Table(
    'Employees', metadata,
    Column('EmployeeID', Integer, primary_key=True, autoincrement=True),
    Column('LastName', String(50)),
    Column('FirstName', String(50)),
    Column('MiddleName', String(50)),
    Column('Position', String(50)),
    Column('Address', String(100)),
    Column('HomePhone', String(20)),
    Column('BirthDate', Date)
)

# Таблица Clients
Clients = Table(
    'Clients', metadata,
    Column('ClientID', Integer, primary_key=True, autoincrement=True),
    Column('FullName', String(100)),
    Column('Address', String(100)),
    Column('Phone', String(20))
)

# Таблица Suppliers
Suppliers = Table(
    'Suppliers', metadata,
    Column('SupplierID', Integer, primary_key=True, autoincrement=True),
    Column('SupplierName', String(100)),
    Column('SupplierRepresentative', String(100)),
    Column('ContactPhone', String(20)),
    Column('Address', String(100))
)

# Таблица Deliveries
Deliveries = Table(
    'Deliveries', metadata,
    Column('DeliveryID', Integer, primary_key=True, autoincrement=True),
    Column('SupplierID', Integer, ForeignKey('Suppliers.SupplierID')),
    Column('DeliveryDate', Date)
)

# Таблица Products
Products = Table(
    'Products', metadata,
    Column('ProductID', Integer, primary_key=True, autoincrement=True),
    Column('DeliveryID', Integer, ForeignKey('Deliveries.DeliveryID')),
    Column('ProductName', String(100)),
    Column('TechnicalSpecifications', String(255)),
    Column('Description', Text),
    Column('Image', Text),
    Column('PurchasePrice', Numeric(10, 2)),
    Column('SalePrice', Numeric(10, 2))
)

# Таблица Orders
Orders = Table(
    'Orders', metadata,
    Column('OrderID', Integer, primary_key=True, autoincrement=True),
    Column('EmployeeID', Integer, ForeignKey('Employees.EmployeeID')),
    Column('ProductID', Integer, ForeignKey('Products.ProductID')),
    Column('OrderDate', Date),
    Column('ExecutionDate', Date),
    Column('ClientID', Integer, ForeignKey('Clients.ClientID'))
)


# Создаем таблицы
metadata.create_all(engine)