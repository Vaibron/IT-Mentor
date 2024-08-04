from sqlalchemy import update, select
from task import Clients, engine

# Создаем соединение с базой данных
with engine.begin() as conn:
    # Находим клиента с ClientID=2
    stmt = select(Clients).where(Clients.c.ClientID == 2)
    client_to_update = conn.execute(stmt).fetchone()

    if client_to_update:
        # Обновляем значения FullName и Phone
        update_stmt = update(Clients).where(Clients.c.ClientID == 2).values(
            FullName='Романова Елизавета',
            Phone='+7(911)123-45-68'
        )
        conn.execute(update_stmt)
        print(f"Данные для клиента с ClientID={client_to_update.ClientID} обновлены.")
    else:
        print("Клиент с ClientID=2 не найден.")