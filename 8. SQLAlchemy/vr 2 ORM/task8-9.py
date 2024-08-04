from task import Employee, Client, Supplier, Delivery, Product, Order, engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

# Создаем фабрику сессий
Session = sessionmaker(bind=engine)

# Создаем сессию
with Session() as session:

    '''8. Получите данные вместе с WHERE, ORDER BY, GROUP BY, DISTINCT и выведите на экран.'''

    # Запросы с WHERE, ORDER BY, GROUP BY, DISTINCT
    print("----- Запрос с WHERE -----")
    employees_with_last_name_ivanov = session.query(Employee).filter(Employee.LastName == 'Иванов').all()
    for employee in employees_with_last_name_ivanov:
        print(f"EmployeeID: {employee.EmployeeID}, LastName: {employee.LastName}, FirstName: {employee.FirstName}")

    print("\n----- Запрос с ORDER BY -----")
    employees_ordered_by_birthdate = session.query(Employee).order_by(Employee.BirthDate).all()
    for employee in employees_ordered_by_birthdate:
        print(
            f"EmployeeID: {employee.EmployeeID}, LastName: {employee.LastName}, FirstName: {employee.FirstName}, BirthDate: {employee.BirthDate}")

    print("\n----- Запрос с GROUP BY -----")
    clients_grouped_by_city = session.query(func.substring(Client.Address, 4, 7).label('City'), func.count('*')).group_by(
        'City').all()
    for city, count in clients_grouped_by_city:
        print(f"City: {city}, Count: {count}")

    print("\n----- Запрос с DISTINCT -----")
    distinct_positions = session.query(Employee.Position).distinct().all()
    for position in distinct_positions:
        print(f"Position: {position[0]}")

# Создание новой сессии для работы с агрегационными функциями
with Session() as session:

    '''9. Примените несколько функций агрегации и выведите результат на экран'''

    # Применение функций агрегации
    print("----- Функции агрегации -----")

    # Средняя цена продажи товаров
    average_sale_price = session.query(func.avg(Product.SalePrice)).scalar()
    print(f"Средняя цена продажи товаров: {average_sale_price}")

    # Количество заказов за определенный период
    orders_count = session.query(func.count(Order.OrderID)).filter(Order.OrderDate >= '2023-12-01').scalar()
    print(f"Количество заказов с 2023-12-01: {orders_count}")

    # Максимальная цена покупки
    max_purchase_price = session.query(func.max(Product.PurchasePrice)).scalar()
    print(f"Максимальная цена покупки: {max_purchase_price}")
