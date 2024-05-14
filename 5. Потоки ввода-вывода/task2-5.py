# Импорт библиотек pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Настройка pandas для отображения максимум 7 строк в выводе
pd.options.display.max_rows = 7
# Установка стиля 'ggplot' для всех графиков matplotlib
plt.style.use('ggplot')
# Установка размера всех графиков на 15x3
plt.rcParams['figure.figsize'] = (15, 3)
# Установка шрифтов для всех графиков на 'sans-serif'
plt.rcParams['font.family'] = 'sans-serif'

# Путь к CSV-файлу с данными о погоде
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/weather_2012.csv'

# Чтение данных из CSV-файла с указанием колонки 'Date/Time (LST)' как индекса и парсингом дат
weather_2012 = pd.read_csv(address, parse_dates=True, index_col='Date/Time (LST)')

# Выборка колонки 'Weather' из датафрейма
weather_description = weather_2012['Weather']
# Создание булевой серии, где True, если в описании погоды есть слово 'Snow'
is_snowing = weather_description.str.contains('Snow')

# Преобразование булевых значений в числовые (True - 1, False - 0)
is_snowing2 = is_snowing.astype(int)
# Построение графика
is_snowing2.plot()
# Отображение графика
plt.show()

# Группировка данных по температуре по месяцам и расчет медианы, построение столбчатого графика
weather_2012['Temp (C)'].resample('ME').median().plot(kind='bar')
# Отображение графика
plt.show()

# Вывод первых 10 значений серии is_snowing после преобразования в числа
print(is_snowing.astype(int)[:10])

# Группировка данных о снегопаде по месяцам и расчет среднего, вывод результатов
print(is_snowing.astype(int).resample('ME').mean())

# Построение столбчатого графика среднего количества снегопадов по месяцам
is_snowing.astype(int).resample('ME').mean().plot(kind='bar')
# Отображение графика
plt.show()

# Группировка и расчет медианы температуры по месяцам
temperature = weather_2012['Temp (C)'].resample('ME').median()
# Повторное создание серии is_snowing для учета обновлений
is_snowing = weather_2012['Weather'].str.contains('Snow')
# Группировка и расчет среднего количества снегопадов по месяцам
snowiness = is_snowing.astype(int).resample('ME').mean()

# Присвоение имён колонкам для удобства
temperature.name = "Temperature"
snowiness.name = "Snowiness"
# Объединение двух серий в один датафрейм по оси колонок
stats = pd.concat([temperature, snowiness], axis=1)
# Вывод статистики
print(stats)
# Построение столбчатого графика для датафрейма stats
stats.plot(kind='bar')
# Отображение графика
plt.show()

# Построение столбчатого графика с подграфиками для каждой колонки датафрейма stats
stats.plot(kind='bar', subplots=True, figsize=(15, 10))
# Отображение графика
plt.show()
