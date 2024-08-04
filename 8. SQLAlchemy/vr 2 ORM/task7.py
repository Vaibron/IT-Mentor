from task import Employee, Client, Supplier, Delivery, Product, Order, Session, engine
from sqlalchemy.orm import sessionmaker

session = Session()

# Обновление данных в таблице Clients
client_to_update = session.query(Client).filter_by(ClientID=2).first()  # Находим клиента с ClientID=2

if client_to_update:
    client_to_update.FullName = 'Романова Мария Ивановна'  # Обновляем значение FullName
    client_to_update.Phone = '+7(911)123-45-68'  # Обновляем значение Phone
    session.commit()  # Сохраняем изменения в базе данных
    print(f"Данные для клиента с ClientID={client_to_update.ClientID} обновлены.")
else:
    print(f"Клиент с ClientID=2 не найден.")

# Закрытие сессии
session.close()
