from task import Employee, Client, Supplier, Delivery, Product, Order, Session, engine

session = Session()

'''10. Удалите несколько строк из таблицы Поставщик и выведите на экран строки этой таблицы'''

print("\n----- Удаление строк из таблицы Поставщик -----")

# Удаление записей из Orders, которые ссылаются на ProductID 2 и 3
session.query(Order).filter(Order.ProductID.in_([2, 3])).delete(synchronize_session='fetch')
session.commit()

# Удаление записей из Products, которые ссылаются на DeliveryID 2 и 3
session.query(Product).filter(Product.DeliveryID.in_([2, 3])).delete(synchronize_session='fetch')
session.commit()

# Удаление записей из Deliveries, которые ссылаются на SupplierID 2 и 3
session.query(Delivery).filter(Delivery.SupplierID.in_([2, 3])).delete(synchronize_session='fetch')
session.commit()

# Удаление строк из таблицы Suppliers
session.query(Supplier).filter(Supplier.SupplierID.in_([2, 3])).delete(synchronize_session='fetch')
session.commit()

# Вывод оставшихся строк таблицы Поставщик
suppliers = session.query(Supplier).all()
print("Оставшиеся строки таблицы Поставщик:")
for supplier in suppliers:
    print(
        f"SupplierID: {supplier.SupplierID}, SupplierName: {supplier.SupplierName}, SupplierRepresentative: {supplier.SupplierRepresentative}, ContactPhone: {supplier.ContactPhone}, Address: {supplier.Address}")

# Закрытие сессии
session.close()
