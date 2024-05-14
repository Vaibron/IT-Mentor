# Импорт библиотеки pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Устанавливаем стиль графиков 'ggplot'
plt.style.use('ggplot')
# Задаем размер для всех графиков
plt.rcParams['figure.figsize'] = (15, 5)

# Указываем путь к файлу CSV
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/bikes.csv'
# Читаем файл CSV в DataFrame pandas, указывая разделитель, кодировку, столбец с датами и порядок даты
fixed_df = pd.read_csv(address,
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
'''
encoding='latin1': Этот аргумент указывает на кодировку символов файла. 
    'latin1' — это тип кодировки, который поддерживает западноевропейский набор символов.
parse_dates=['Date']: Указывает, что столбец 'Date' должен быть проанализирован как дата, 
    что позволяет использовать даты в качестве временных меток в DataFrame.
dayfirst=True: Этот аргумент говорит функции, что первым в дате идет день, а не месяц, 
    что важно для правильного преобразования строк в даты, особенно когда данные содержат даты в формате, отличном от американского стандарта (где месяц идет первым).
index_col='Date': Определяет столбец 'Date' как индекс DataFrame, 
    что позволяет выполнять операции с данными, используя даты в качестве ключей.
'''

# Выводим первые 3 строки DataFrame
print(fixed_df[:3])  # Можно также использовать fixed_df.head(3)

# Выводим первые 10 значений из столбца 'Berri 1'
print(fixed_df['Berri 1'][:10])

# Строим график по данным из столбца 'Berri 1'
fixed_df['Berri 1'].plot()

# Добавляем подписи к осям и заголовок графика
plt.xlabel('Дата')
plt.ylabel('Количество')
plt.title('График поездок на велосипеде по датам')

# Отображаем график
plt.show()  # Если указать block=True, программа будет ждать закрытия окна графика

# Строим график по всем данным DataFrame
fixed_df.plot(figsize=(17, 9))  # Изменяем размер окна графика
plt.show()

# Вычисляем сумму значений по столбцу 'Rachel1'
column_sum = fixed_df['Rachel1'].sum()
print(column_sum)

