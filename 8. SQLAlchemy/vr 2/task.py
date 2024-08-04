from sqlalchemy import create_engine, String, Date, ForeignKey, Text, Numeric
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column, sessionmaker

# Создание подключения к базе данных
engine = create_engine('postgresql://postgres:5981@localhost:5432/new_db', echo=True)

# Создание базового класса для моделей
Base = declarative_base()

# Создание сессии
Session = sessionmaker(bind=engine)

# Модель Employees
class Employee(Base):
    __tablename__ = 'Employees'

    EmployeeID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    LastName: Mapped[str] = mapped_column(String(50))
    FirstName: Mapped[str] = mapped_column(String(50))
    MiddleName: Mapped[str] = mapped_column(String(50))
    Position: Mapped[str] = mapped_column(String(50))
    Address: Mapped[str] = mapped_column(String(100))
    HomePhone: Mapped[str] = mapped_column(String(20))
    BirthDate: Mapped[Date] = mapped_column(Date)

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="employee")


# Модель Clients
class Client(Base):
    __tablename__ = 'Clients'

    ClientID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    FullName: Mapped[str] = mapped_column(String(100))
    Address: Mapped[str] = mapped_column(String(100))
    Phone: Mapped[str] = mapped_column(String(20))

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="client")


# Модель Suppliers
class Supplier(Base):
    __tablename__ = 'Suppliers'

    SupplierID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    SupplierName: Mapped[str] = mapped_column(String(100))
    SupplierRepresentative: Mapped[str] = mapped_column(String(100))
    ContactPhone: Mapped[str] = mapped_column(String(20))
    Address: Mapped[str] = mapped_column(String(100))

    deliveries: Mapped[list["Delivery"]] = relationship("Delivery", back_populates="supplier")


# Модель Deliveries
class Delivery(Base):
    __tablename__ = 'Deliveries'

    DeliveryID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    SupplierID: Mapped[int] = mapped_column(ForeignKey('Suppliers.SupplierID'))
    DeliveryDate: Mapped[Date] = mapped_column(Date)

    supplier: Mapped["Supplier"] = relationship("Supplier", back_populates="deliveries")
    products: Mapped[list["Product"]] = relationship("Product", back_populates="delivery")


# Модель Products
class Product(Base):
    __tablename__ = 'Products'

    ProductID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    DeliveryID: Mapped[int] = mapped_column(ForeignKey('Deliveries.DeliveryID'))
    ProductName: Mapped[str] = mapped_column(String(100))
    TechnicalSpecifications: Mapped[str] = mapped_column(String(255))
    Description: Mapped[str] = mapped_column(Text)
    Image: Mapped[str] = mapped_column(Text)
    PurchasePrice: Mapped[Numeric] = mapped_column(Numeric(10, 2))
    SalePrice: Mapped[Numeric] = mapped_column(Numeric(10, 2))

    delivery: Mapped["Delivery"] = relationship("Delivery", back_populates="products")
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="product")


# Модель Orders
class Order(Base):
    __tablename__ = 'Orders'

    OrderID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    EmployeeID: Mapped[int] = mapped_column(ForeignKey('Employees.EmployeeID'))
    ProductID: Mapped[int] = mapped_column(ForeignKey('Products.ProductID'))
    OrderDate: Mapped[Date] = mapped_column(Date)
    ExecutionDate: Mapped[Date] = mapped_column(Date)
    ClientID: Mapped[int] = mapped_column(ForeignKey('Clients.ClientID'))

    employee: Mapped["Employee"] = relationship("Employee", back_populates="orders")
    product: Mapped["Product"] = relationship("Product", back_populates="orders")
    client: Mapped["Client"] = relationship("Client", back_populates="orders")


# Создание таблиц в базе данных
Base.metadata.create_all(engine)
