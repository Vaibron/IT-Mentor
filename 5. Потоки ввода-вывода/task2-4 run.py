import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

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

weather_2012_final = pd.read_csv(address, index_col='Date/Time (LST)')
weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
plt.show()
