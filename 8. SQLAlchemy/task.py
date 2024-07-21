'''2. Создайте новую бд. Напишите коннектор для подключения к базе данных postgresql.'''
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text, Numeric, inspect
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Создание подключения к базе данных
engine = create_engine('postgresql://postgres:5981@localhost:5432/new_db')

'''3. Создайте Классы моделей, которые будут реализовывать схему данных на прикрепленном рисунке.'''
# Создание базового класса для моделей
Base = declarative_base()


# Модель Employees
class Employee(Base):
    __tablename__ = 'Employees'

    EmployeeID = Column(Integer, primary_key=True, autoincrement=True)
    LastName = Column(String(50))
    FirstName = Column(String(50))
    MiddleName = Column(String(50))
    Position = Column(String(50))
    Address = Column(String(100))
    HomePhone = Column(String(20))
    BirthDate = Column(Date)

    orders = relationship("Order", back_populates="employee")


# Модель Clients
class Client(Base):
    __tablename__ = 'Clients'

    ClientID = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement=True
    FullName = Column(String(100))
    Address = Column(String(100))
    Phone = Column(String(20))

    orders = relationship("Order", back_populates="client")


# Модель Suppliers
class Supplier(Base):
    __tablename__ = 'Suppliers'

    SupplierID = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement=True
    SupplierName = Column(String(100))
    SupplierRepresentative = Column(String(100))
    ContactPhone = Column(String(20))
    Address = Column(String(100))

    deliveries = relationship("Delivery", back_populates="supplier")


# Модель Deliveries
class Delivery(Base):
    __tablename__ = 'Deliveries'

    DeliveryID = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement=True
    SupplierID = Column(Integer, ForeignKey('Suppliers.SupplierID'))
    DeliveryDate = Column(Date)

    supplier = relationship("Supplier", back_populates="deliveries")
    products = relationship("Product", back_populates="delivery")


# Модель Products
class Product(Base):
    __tablename__ = 'Products'

    ProductID = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement=True
    DeliveryID = Column(Integer, ForeignKey('Deliveries.DeliveryID'))
    ProductName = Column(String(100))
    TechnicalSpecifications = Column(String(255))
    Description = Column(Text)
    Image = Column(Text)
    PurchasePrice = Column(Numeric(10, 2))
    SalePrice = Column(Numeric(10, 2))

    delivery = relationship("Delivery", back_populates="products")
    orders = relationship("Order", back_populates="product")


# Модель Orders
class Order(Base):
    __tablename__ = 'Orders'

    OrderID = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement=True
    EmployeeID = Column(Integer, ForeignKey('Employees.EmployeeID'))
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    OrderDate = Column(Date)
    ExecutionDate = Column(Date)
    ClientID = Column(Integer, ForeignKey('Clients.ClientID'))

    employee = relationship("Employee", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    client = relationship("Client", back_populates="orders")


# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблиц в базе данных (только если их нет)
if not inspect(engine).has_table('Employees'):
    Base.metadata.create_all(engine)

# Закрытие сессии
session.close()
