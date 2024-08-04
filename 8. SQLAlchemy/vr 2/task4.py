from datetime import date
from task import Employee, Client, Supplier, Delivery, Product, Order, Session


with Session() as session:
    # Добавление сотрудников
    employees = [
        Employee(LastName='Иванов', FirstName='Иван', MiddleName='Иванович', Position='Менеджер',
                 Address='г. Москва, ул. Ленина, д. 1', HomePhone='+7(900)123-45-67', BirthDate=date(1990, 1, 1)),
        Employee(LastName='Петров', FirstName='Петр', MiddleName='Петрович', Position='Продавец',
                 Address='г. Санкт-Петербург, ул. Невского, д. 2', HomePhone='+7(911)123-45-67', BirthDate=date(1985, 2, 15)),
        Employee(LastName='Сидоров', FirstName='Сидор', MiddleName='Сидорович', Position='Курьер',
                 Address='г. Екатеринбург, ул. 8 Марта, д. 3', HomePhone='+7(922)123-45-67', BirthDate=date(1995, 3, 20)),
        Employee(LastName='Кузнецов', FirstName='Кузьма', MiddleName='Кузьмич', Position='Оператор',
                 Address='г. Нижний Новгород, ул. Большая Покровская, д. 4', HomePhone='+7(929)123-45-67', BirthDate=date(1980, 4, 25)),
        Employee(LastName='Смирнов', FirstName='Семён', MiddleName='Семёнович', Position='Кладовщик',
                 Address='г. Челябинск, ул. Кирова, д. 5', HomePhone='+7(914)123-45-67', BirthDate=date(1975, 5, 30))
    ]
    session.add_all(employees)

    # Добавление клиентов
    clients = [
        Client(FullName='Козлов Алексей', Address='г. Москва, ул. Пушкина, д. 1', Phone='+7(903)123-45-67'),
        Client(FullName='Романова Мария', Address='г. Санкт-Петербург, ул. Лермонтова, д. 2', Phone='+7(911)123-45-67'),
        Client(FullName='Соколов Дмитрий', Address='г. Екатеринбург, ул. Чехова, д. 3', Phone='+7(922)123-45-67'),
        Client(FullName='Петрова Ольга', Address='г. Нижний Новгород, ул. Гоголя, д. 4', Phone='+7(929)123-45-67'),
        Client(FullName='Иванов Сергей', Address='г. Челябинск, ул. Тургенева, д. 5', Phone='+7(914)123-45-67')
    ]
    session.add_all(clients)

    # Добавление поставщиков
    suppliers = [
        Supplier(SupplierName='Компания А', SupplierRepresentative='Иванов Иван', ContactPhone='+7(900)123-45-67', Address='г. Москва, ул. Ленина, д. 1'),
        Supplier(SupplierName='Компания Б', SupplierRepresentative='Петров Петр', ContactPhone='+7(911)123-45-67', Address='г. Санкт-Петербург, ул. Невского, д. 2'),
        Supplier(SupplierName='Компания В', SupplierRepresentative='Сидоров Сидор', ContactPhone='+7(922)123-45-67', Address='г. Екатеринбург, ул. 8 Марта, д. 3'),
        Supplier(SupplierName='Компания Г', SupplierRepresentative='Кузнецов Кузьма', ContactPhone='+7(929)123-45-67', Address='г. Нижний Новгород, ул. Большая Покровская, д. 4'),
        Supplier(SupplierName='Компания Д', SupplierRepresentative='Смирнов Семён', ContactPhone='+7(914)123-45-67', Address='г. Челябинск, ул. Кирова, д. 5')
    ]
    session.add_all(suppliers)

    # Добавление поставок
    deliveries = [
        Delivery(SupplierID=1, DeliveryDate=date(2023, 12, 1)),
        Delivery(SupplierID=2, DeliveryDate=date(2023, 12, 5)),
        Delivery(SupplierID=3, DeliveryDate=date(2023, 12, 10)),
        Delivery(SupplierID=4, DeliveryDate=date(2023, 12, 15)),
        Delivery(SupplierID=5, DeliveryDate=date(2023, 12, 20))
    ]
    session.add_all(deliveries)

    # Добавление продуктов
    products = [
        Product(DeliveryID=1, ProductName='Товар 1', TechnicalSpecifications='Технические характеристики 1', Description='Описание товара 1', Image='image1.jpg', PurchasePrice=100.00, SalePrice=150.00),
        Product(DeliveryID=2, ProductName='Товар 2', TechnicalSpecifications='Технические характеристики 2', Description='Описание товара 2', Image='image2.jpg', PurchasePrice=200.00, SalePrice=250.00),
        Product(DeliveryID=3, ProductName='Товар 3', TechnicalSpecifications='Технические характеристики 3', Description='Описание товара 3', Image='image3.jpg', PurchasePrice=300.00, SalePrice=350.00),
        Product(DeliveryID=4, ProductName='Товар 4', TechnicalSpecifications='Технические характеристики 4', Description='Описание товара 4', Image='image4.jpg', PurchasePrice=400.00, SalePrice=450.00),
        Product(DeliveryID=5, ProductName='Товар 5', TechnicalSpecifications='Технические характеристики 5', Description='Описание товара 5', Image='image5.jpg', PurchasePrice=500.00, SalePrice=550.00)
    ]
    session.add_all(products)

    # Добавление заказов
    orders = [
        Order(EmployeeID=1, ProductID=1, OrderDate=date(2023, 12, 1), ExecutionDate=date(2023, 12, 2), ClientID=1),
        Order(EmployeeID=2, ProductID=2, OrderDate=date(2023, 12, 5), ExecutionDate=date(2023, 12, 6), ClientID=2),
        Order(EmployeeID=3, ProductID=3, OrderDate=date(2023, 12, 10), ExecutionDate=date(2023, 12, 11), ClientID=3),
        Order(EmployeeID=4, ProductID=4, OrderDate=date(2023, 12, 15), ExecutionDate=date(2023, 12, 16), ClientID=4),
        Order(EmployeeID=5, ProductID=5, OrderDate=date(2023, 12, 20), ExecutionDate=date(2023, 12, 21), ClientID=5)
    ]
    session.add_all(orders)

    # Фиксация всех изменений
    session.commit()
