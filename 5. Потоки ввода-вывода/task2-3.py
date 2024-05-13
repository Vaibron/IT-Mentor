import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/bikes.csv'
bikes = pd.read_csv(address,
                    sep=',', encoding='latin1',
                    parse_dates=['Date'], dayfirst=True,
                    index_col='Date')

# Выводим график только по столбцу Berri 1
# bikes['Berri 1'].plot()
# plt.show()

# создаем переменную berri_bikes которая хранит в себе данные из столбца Berri 1
berri_bikes = bikes[['Berri 1']].copy()

# Выводим первые 5 строк нашей переменной
print(berri_bikes[:5])

# Выводим все индексы переменной berri_bikes
print(berri_bikes.index)

# Выводим только дни в индексах переменной berri_bikes
print(berri_bikes.index.day)

# Выводим номер дня недели в индексах переменной berri_bikes
print(berri_bikes.index.weekday)

# Добавляем новый столбец с днями недели в berri_bikes
berri_bikes.loc[:, 'Weekday'] = berri_bikes.index.weekday
print(berri_bikes[:5])

# Создаем новую переменную weekday_counts в которой будут хранится сгруппированные данные по дням неделе и кол-ве
weekday_counts = berri_bikes.groupby('Weekday').sum()
# можно и так - weekday_counts = berri_bikes.groupby('Weekday').aggregate(sum)
print(weekday_counts)

# Теперь переименуем 0, 1, 2, 3, 4, 5, 6, чтобы понимать, что они означают:
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)

# Строим график
weekday_counts.plot(kind='bar')
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