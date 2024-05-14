# Импорт библиотеки pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Устанавливаем стиль 'ggplot'
plt.style.use('ggplot')
# Задаем размер для всех графиков
plt.rcParams['figure.figsize'] = (10, 5)

# Задаем путь к файлу CSV
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/311-service-requests.csv'
# Читаем файл CSV в DataFrame pandas
complaints = pd.read_csv(address, low_memory=False)
# Параметр low_memory=False используется для предотвращения предупреждений о смешанных типах данных в столбцах
# Выводим содержимое DataFrame
print(complaints)

# Выводим первые 5 строк DataFrame
print(complaints[:5])

# Выводим первые 5 значений столбца 'Complaint Type'
print(complaints['Complaint Type'][:5])  # Альтернативный способ: complaints[:5]['Complaint Type']

# Выводим первые 10 строк для столбцов 'Complaint Type' и 'Borough'
print(complaints[['Complaint Type', 'Borough']][:10])

# Выводим количество уникальных значений в столбце 'Complaint Type'
print(complaints['Complaint Type'].value_counts())

# Сохраняем 10 наиболее частых жалоб в переменную и выводим их
complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts[:10])

# Строим столбчатую диаграмму для 10 наиболее частых жалоб
complaint_counts[:10].plot(kind='bar')
# Отображаем график
plt.show()
