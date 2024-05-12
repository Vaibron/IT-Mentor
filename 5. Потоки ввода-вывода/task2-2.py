import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

address = '/Users/aleksejsypko/Desktop/Python/PycharmProjects/5. Потоки ввода-вывода/311-service-requests.csv'
complaints = pd.read_csv(address)
print(complaints)

# срез 5 строк
print(complaints[:5])

# срез 5 строк, столбца Complaint Typ
print(complaints['Complaint Type'][:5])  # можно так complaints[:5]['Complaint Type']

# Выбор нескольких столбцов (две пары квадратных скобок) + срез 10 строк
print(complaints[['Complaint Type', 'Borough']][:10])

# самый частый тип по столбцу Complaint Type
print(complaints['Complaint Type'].value_counts())

# 10 наиболее частых типов:
complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts[:10])

# Строим график
complaint_counts[:10].plot(kind='bar')  # Чтобы построить столбчатую диаграмму, необходимо добавить аргумент kind='bar'
plt.show()