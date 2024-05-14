# Импорт библиотеки pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Установка максимального количества отображаемых строк в pandas DataFrame на 7
pd.options.display.max_rows = 7
# Установка стиля 'ggplot' для графиков
plt.style.use('ggplot')
# Установка размера всех графиков на 15x3
plt.rcParams['figure.figsize'] = (15, 3)
# Установка шрифтов для всех графиков на 'sans-serif'
plt.rcParams['font.family'] = 'sans-serif'

# Шаблон адреса для загрузки данных о погоде с сайта Environment Canada
url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
# Формирование адреса с использованием шаблона и подстановкой месяца и года
url = url_template.format(month=3, year=2012)
# Загрузка данных о погоде за март 2012 года с сайта
weather_mar2012 = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='utf-8-sig')
# Вывод загруженных данных в консоль
print(weather_mar2012)

# Построение графика изменения температуры в марте 2012 года
weather_mar2012["Temp (°C)"].plot(figsize=(15, 5))
# Отображение графика
plt.show()

# Удаление ненужных столбцов из DataFrame
weather_mar2012 = weather_mar2012.drop(['Longitude (x)', 'Latitude (y)', 'Station Name', 'Climate ID', 'Precip. Amount (mm)', 'Precip. Amount Flag'], axis=1)

# Переименование столбцов для удобства работы с данными
weather_mar2012.columns = [
 u'Year', u'Month', u'Day', u'Time', u'Temp (C)',
 u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag',
 u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag',
 u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
 u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill',
 u'Wind Chill Flag', u'Weather']

# Удаление столбцов с пустыми значениями
weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')

# Удаление столбцов с датой и временем, так как они уже используются в качестве индекса
weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time'], axis=1)

# Создание копии DataFrame только с данными о температуре
temperatures = weather_mar2012[['Temp (C)']].copy()
# Добавление столбца 'Hour' с часом из индекса (время суток)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
# Группировка данных по часам и расчет медианной температуры для каждого часа
temperatures.groupby('Hour').aggregate('median').plot()
# Отображение графика
plt.show()
