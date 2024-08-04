from task import engine, Orders, Products, Deliveries, Suppliers
from sqlalchemy import delete, select

# Удаление записей из Orders, которые ссылаются на ProductID 2 и 3
with engine.connect() as connection:
    delete_orders = delete(Orders).where(Orders.c.ProductID.in_([2, 3]))
    connection.execute(delete_orders)
    connection.commit()

# Удаление записей из Products, которые ссылаются на DeliveryID 2 и 3
    delete_products = delete(Products).where(Products.c.DeliveryID.in_([2, 3]))
    connection.execute(delete_products)
    connection.commit()

# Удаление записей из Deliveries, которые ссылаются на SupplierID 2 и 3
    delete_deliveries = delete(Deliveries).where(Deliveries.c.SupplierID.in_([2, 3]))
    connection.execute(delete_deliveries)
    connection.commit()

# Удаление строк из таблицы Suppliers
    delete_suppliers = delete(Suppliers).where(Suppliers.c.SupplierID.in_([2, 3]))
    connection.execute(delete_suppliers)
    connection.commit()

# Вывод оставшихся строк таблицы Suppliers
    select_suppliers = select(Suppliers)
    result = connection.execute(select_suppliers)

    print("Оставшиеся строки таблицы Suppliers:")
    for row in result:
        print(row)