# Импортируем библиотеку pandas и matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# Устанавливаем стиль 'ggplot' для графиков
plt.style.use('ggplot')
# Задаем размер фигуры для всех графиков
plt.rcParams['figure.figsize'] = (15, 5)

# Определяем переменную 'address', содержащую путь к текстовому файлу с данными
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/popularity-contest.txt'
# Читаем данные из файла, используя пробел в качестве разделителя, и исключаем последнюю строку ([:-1])
popcon = pd.read_csv(address, sep=' ')[:-1]
# Задаем названия столбцов для DataFrame
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
# Выводим первые пять строк DataFrame для предварительного просмотра
print(popcon[:5])

# Преобразуем значения в столбцах 'atime' и 'ctime' из строк в целые числа
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

# Преобразуем целочисленные значения в столбцах 'atime' и 'ctime' в формат даты и времени
popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

# Выводим тип данных столбца 'atime' и снова первые пять строк DataFrame
print(popcon['atime'].dtype)
print(popcon[:5])

# Фильтруем DataFrame, оставляя только те строки, где 'atime' больше 1 января 1970 года
popcon = popcon[popcon['atime'] > '1970-01-01']

# Создаем новый DataFrame 'nonlibraries', исключая строки, где в названии пакета содержится 'lib'
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

# Сортируем 'nonlibraries' по убыванию времени создания ('ctime') и выводим первые 10 строк
print(nonlibraries.sort_values('ctime', ascending=False)[:10])
