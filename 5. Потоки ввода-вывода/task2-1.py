import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

address = '/Users/aleksejsypko/Desktop/Python/PycharmProjects/5. Потоки ввода-вывода/bikes.csv'
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

print(fixed_df[:3])  # можно так - fixed_df.head(3)

print(fixed_df['Berri 1'][:10])  # Получаем данные из столбца Berri 1 - 10 строк

# Выводим график по столбцу Berri 1 по датам
fixed_df['Berri 1'].plot()

# Добавляем подписи к осям и заголовок:
plt.xlabel('Дата')
plt.ylabel('Кол-во')
plt.title('График')

plt.show()  # Аргумент block=True программа останавливается, пока график не будет закрыт пользователем.

# Выводим график всей таблицы по датам
fixed_df.plot(figsize=(17, 9))  # figsize=(17, 9) - меняем размер окна
plt.show()

# Сумма по столбцу Rachel1
column_sum = fixed_df['Rachel1'].sum()
print(column_sum)
