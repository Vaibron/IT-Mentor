import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'


url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='utf-8-sig')
#print(weather_mar2012)

# Диаграмма
# weather_mar2012["Temp (°C)"].plot(figsize=(15, 5))
# plt.show()

# Удаляем лишние столбцы
weather_mar2012 = weather_mar2012.drop(['Longitude (x)', 'Latitude (y)', 'Station Name', 'Climate ID', 'Precip. Amount (mm)', 'Precip. Amount Flag'], axis=1)

# Исправляем названия некоторых столбцов
weather_mar2012.columns = [
 u'Year', u'Month', u'Day', u'Time', u'Temp (C)',
 u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag',
 u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag',
 u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
 u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill',
 u'Wind Chill Flag', u'Weather']

# удаляем столбцы, если хотя бы одно значение пусто".
weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')

# удаляем столбцы 'Year', 'Month', 'Day', 'Time'
weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time'], axis=1)


# Выводим дневной график температуры
temperatures = weather_mar2012[['Temp (C)']].copy()
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate('median').plot()
plt.show()

def download_weather_month(year, month):
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='utf-8-sig')
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year','Day','Month','Time (LST)','Longitude (x)',
                                      'Latitude (y)','Station Name','Climate ID', ], axis=1)
    return weather_data



data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]
weather_2012 = pd.concat(data_by_month)

address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/weather_2012.csv'
weather_2012.to_csv(address)
