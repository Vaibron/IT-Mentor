from task import Employees, Clients, Suppliers, Deliveries, Products, Orders, engine
from sqlalchemy import insert

# Employees
stmts = [
    # Employees
    insert(Employees).values([
        {'LastName': 'Иванов', 'FirstName': 'Иван', 'MiddleName': 'Иванович', 'Position': 'Менеджер',
         'Address': 'г. Москва, ул. Ленина, д. 1', 'HomePhone': '+7(900)123-45-67', 'BirthDate': '1990-01-01'},
        {'LastName': 'Петров', 'FirstName': 'Петр', 'MiddleName': 'Петрович', 'Position': 'Продавец',
         'Address': 'г. Санкт-Петербург, ул. Невского, д. 2', 'HomePhone': '+7(911)123-45-67', 'BirthDate': '1985-02-15'},
        {'LastName': 'Сидоров', 'FirstName': 'Сидор', 'MiddleName': 'Сидорович', 'Position': 'Курьер',
         'Address': 'г. Екатеринбург, ул. 8 Марта, д. 3', 'HomePhone': '+7(922)123-45-67', 'BirthDate': '1995-03-20'},
        {'LastName': 'Кузнецов', 'FirstName': 'Кузьма', 'MiddleName': 'Кузьмич', 'Position': 'Оператор',
         'Address': 'г. Нижний Новгород, ул. Большая Покровская, д. 4', 'HomePhone': '+7(929)123-45-67', 'BirthDate': '1980-04-25'},
        {'LastName': 'Смирнов', 'FirstName': 'Семён', 'MiddleName': 'Семёнович', 'Position': 'Кладовщик',
         'Address': 'г. Челябинск, ул. Кирова, д. 5', 'HomePhone': '+7(914)123-45-67', 'BirthDate': '1975-05-30'}
    ]),
    insert(Clients).values([
        {'FullName': 'Козлов Алексей', 'Address': 'г. Москва, ул. Пушкина, д. 1', 'Phone': '+7(903)123-45-67'},
        {'FullName': 'Романова Мария', 'Address': 'г. Санкт-Петербург, ул. Лермонтова, д. 2', 'Phone': '+7(911)123-45-67'},
        {'FullName': 'Соколов Дмитрий', 'Address': 'г. Екатеринбург, ул. Чехова, д. 3', 'Phone': '+7(922)123-45-67'},
        {'FullName': 'Петрова Ольга', 'Address': 'г. Нижний Новгород, ул. Гоголя, д. 4', 'Phone': '+7(929)123-45-67'},
        {'FullName': 'Иванов Сергей', 'Address': 'г. Челябинск, ул. Тургенева, д. 5', 'Phone': '+7(914)123-45-67'}
    ]),
    insert(Suppliers).values([
        {'SupplierName': 'Компания А', 'SupplierRepresentative': 'Иванов Иван', 'ContactPhone': '+7(900)123-45-67',
         'Address': 'г. Москва, ул. Ленина, д. 1'},
        {'SupplierName': 'Компания Б', 'SupplierRepresentative': 'Петров Петр', 'ContactPhone': '+7(911)123-45-67',
         'Address': 'г. Санкт-Петербург, ул. Невского, д. 2'},
        {'SupplierName': 'Компания В', 'SupplierRepresentative': 'Сидоров Сидор', 'ContactPhone': '+7(922)123-45-67',
         'Address': 'г. Екатеринбург, ул. 8 Марта, д. 3'},
        {'SupplierName': 'Компания Г', 'SupplierRepresentative': 'Кузнецов Кузьма', 'ContactPhone': '+7(929)123-45-67',
         'Address': 'г. Нижний Новгород, ул. Большая Покровская, д. 4'},
        {'SupplierName': 'Компания Д', 'SupplierRepresentative': 'Смирнов Семён', 'ContactPhone': '+7(914)123-45-67',
         'Address': 'г. Челябинск, ул. Кирова, д. 5'}
    ]),
    insert(Deliveries).values([
        {'SupplierID': 1, 'DeliveryDate': '2023-12-01'},
        {'SupplierID': 2, 'DeliveryDate': '2023-12-05'},
        {'SupplierID': 3, 'DeliveryDate': '2023-12-10'},
        {'SupplierID': 4, 'DeliveryDate': '2023-12-15'},
        {'SupplierID': 5, 'DeliveryDate': '2023-12-20'}
    ]),
    insert(Products).values([
        {'DeliveryID': 1, 'ProductName': 'Товар 1', 'TechnicalSpecifications': 'Технические характеристики 1',
         'Description': 'Описание товара 1', 'Image': 'image1.jpg', 'PurchasePrice': 100.00, 'SalePrice': 150.00},
        {'DeliveryID': 2, 'ProductName': 'Товар 2', 'TechnicalSpecifications': 'Технические характеристики 2',
         'Description': 'Описание товара 2', 'Image': 'image2.jpg', 'PurchasePrice': 200.00, 'SalePrice': 250.00},
        {'DeliveryID': 3, 'ProductName': 'Товар 3', 'TechnicalSpecifications': 'Технические характеристики 3',
         'Description': 'Описание товара 3', 'Image': 'image3.jpg', 'PurchasePrice': 300.00, 'SalePrice': 350.00},
        {'DeliveryID': 4, 'ProductName': 'Товар 4', 'TechnicalSpecifications': 'Технические характеристики 4',
         'Description': 'Описание товара 4', 'Image': 'image4.jpg', 'PurchasePrice': 400.00, 'SalePrice': 450.00},
        {'DeliveryID': 5, 'ProductName': 'Товар 5', 'TechnicalSpecifications': 'Технические характеристики 5',
         'Description': 'Описание товара 5', 'Image': 'image5.jpg', 'PurchasePrice': 500.00, 'SalePrice': 550.00}
    ]),
    insert(Orders).values([
        {'EmployeeID': 1, 'ProductID': 1, 'OrderDate': '2023-12-01', 'ExecutionDate': '2023-12-02', 'ClientID': 1},
        {'EmployeeID': 2, 'ProductID': 2, 'OrderDate': '2023-12-05', 'ExecutionDate': '2023-12-06', 'ClientID': 2},
        {'EmployeeID': 3, 'ProductID': 3, 'OrderDate': '2023-12-10', 'ExecutionDate': '2023-12-11', 'ClientID': 3},
        {'EmployeeID': 4, 'ProductID': 4, 'OrderDate': '2023-12-15', 'ExecutionDate': '2023-12-16', 'ClientID': 4},
        {'EmployeeID': 5, 'ProductID': 5, 'OrderDate': '2023-12-20', 'ExecutionDate': '2023-12-21', 'ClientID': 5}
    ])
]


with engine.begin() as conn:
    for stmt in stmts:
        conn.execute(stmt)
