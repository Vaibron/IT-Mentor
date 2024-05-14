# Импортируем библиотеку pandas
import pandas as pd
# Импортируем библиотеку matplotlib.pyplot для визуализации данных
import matplotlib.pyplot as plt
# Импортируем библиотеку numpy для численных операций
import numpy as np

# Устанавливаем максимальное количество отображаемых строк в pandas
pd.options.display.max_rows = 7
# Устанавливаем стиль 'ggplot' для графиков matplotlib
plt.style.use('ggplot')
# Устанавливаем размер фигуры для графиков matplotlib
plt.rcParams['figure.figsize'] = (15, 3)
# Устанавливаем семейство шрифтов для графиков matplotlib
plt.rcParams['font.family'] = 'sans-serif'

# Задаём путь к файлу CSV
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/311-service-requests.csv'
# Читаем файл CSV и сохраняем его в переменную requests
requests = pd.read_csv(address)

# Выводим уникальные значения почтовых индексов из столбца 'Incident Zip'
print(requests['Incident Zip'].unique())

# Задаём значения, которые будут интерпретироваться как NaN (не числа)
na_values = ['NO CLUE', 'N/A', '0']
# Читаем файл CSV снова, на этот раз указывая значения na_values и тип данных для столбца 'Incident Zip'
requests = pd.read_csv(address, na_values=na_values, dtype={'Incident Zip': str})

# Выводим уникальные значения почтовых индексов после обработки na_values
print(requests['Incident Zip'].unique())

# Находим строки, где почтовые индексы содержат дефис, и заменяем NaN на False
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
# Выводим количество таких строк и сами значения
print(len(requests[rows_with_dashes]))
print(requests[rows_with_dashes]['Incident Zip'])

# Находим почтовые индексы длиннее 5 символов
long_zip_codes = requests['Incident Zip'].str.len() > 5
# Выводим уникальные значения таких индексов
print(requests['Incident Zip'][long_zip_codes].unique())

# Обрезаем почтовые индексы до первых 5 символов
requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
# Выводим строки, где почтовый индекс равен '00000'
print(requests[requests['Incident Zip'] == '00000'])

# Заменяем '00000' на NaN
zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan
# Выводим уникальные значения почтовых индексов после замены
unique_zips = requests['Incident Zip'].unique()
print(unique_zips)

# Сохраняем столбец 'Incident Zip' в переменную zips
zips = requests['Incident Zip']
# Предполагаем, что индексы, начинающиеся на '0' или '1', являются корректными
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# Определяем индексы, не начинающиеся на '0' или '1' и не являющиеся NaN
is_far = ~(is_close) & zips.notnull()
# Выводим такие индексы
print(zips[is_far])

# Выводим строки с такими индексами, сортируя их по индексу
print(requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip'))

# Выводим количество упоминаний каждого города, приведя названия городов к верхнему регистру
print(requests['City'].str.upper().value_counts())
