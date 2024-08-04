from task import Employees, Clients, engine
from sqlalchemy import select, func, distinct

'''8. Получите данные вместе с WHERE, ORDER BY, GROUP BY, DISTINCT и выведите на экран.'''

# Запросы с WHERE, ORDER BY, GROUP BY, DISTINCT
print("----- Запрос с WHERE -----")
with engine.begin() as conn:
    result = conn.execute(select(Employees).where(Employees.c.LastName == 'Иванов')).all()

    for row in result:
        print(row)

print("\n----- Запрос с ORDER BY -----")
with engine.begin() as conn:
    result = conn.execute(select(Employees).order_by(Employees.c.BirthDate))

    for row in result:
        print(row)

print("\n----- Запрос с GROUP BY -----")
with engine.begin() as conn:
    result = conn.execute(
        select(
            func.substring(Clients.c.Address, 4, 7).label('City'),
            func.count('*').label('Count')
        ).group_by('City')
    ).all()

    for row in result:
        print(row)

print("\n----- Запрос с DISTINCT -----")
with engine.begin() as conn:
    result = conn.execute(
        select(
            distinct(Employees.c.Position)
        )
    ).all()

    for row in result:
        print(row)
