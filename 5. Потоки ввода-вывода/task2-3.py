# Импорт библиотеки pandas, matplotlib и numpy
import pandas as pd
import matplotlib.pyplot as plt

# Установка стиля графиков 'ggplot'
plt.style.use('ggplot')
# Установка размера графиков по умолчанию на 10x5
plt.rcParams['figure.figsize'] = (10, 5)

# Путь к файлу CSV
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/bikes.csv'
# Чтение данных из CSV-файла, разделенных запятыми, с указанием кодировки, парсингом даты и установкой колонки 'Date' в качестве индекса
bikes = pd.read_csv(address, sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

# Создание переменной berri_bikes, которая содержит данные только из столбца 'Berri 1'
berri_bikes = bikes[['Berri 1']].copy()

# Вывод первых 5 строк переменной berri_bikes
print(berri_bikes[:5])

# Вывод всех индексов (дат) переменной berri_bikes
print(berri_bikes.index)

# Вывод дней месяца для всех индексов переменной berri_bikes
print(berri_bikes.index.day)

# Вывод номеров дней недели для всех индексов переменной berri_bikes (0 - понедельник, 6 - воскресенье)
print(berri_bikes.index.weekday)

# Добавление нового столбца 'Weekday' в DataFrame berri_bikes, содержащего номера дней недели
berri_bikes.loc[:, 'Weekday'] = berri_bikes.index.weekday
print(berri_bikes[:5])

# Группировка данных по дням недели и подсчет суммы по каждому дню
weekday_counts = berri_bikes.groupby('Weekday').sum()
print(weekday_counts)

# Переименование индексов для понимания, какому дню недели соответствует каждое число
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)

# Построение столбчатой диаграммы
weekday_counts.plot(kind='bar')
# Отображение графика
plt.show()


"""
# Код без пояснений

address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/bikes.csv'
bikes = pd.read_csv(address,
                    sep=',', encoding='latin1',
                    parse_dates=['Date'], dayfirst=True,
                    index_col='Date')

berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:, 'Weekday'] = berri_bikes.index.weekday
weekday_counts = berri_bikes.groupby('Weekday').sum()    # можно и так - weekday_counts = berri_bikes.groupby('Weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')
plt.show()

"""