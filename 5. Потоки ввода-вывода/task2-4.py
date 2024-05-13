import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

# address = '/Users/aleksejsypko/Desktop/Python/PycharmProjects/5. Потоки ввода-вывода/'
# weather_2012_final = pd.read_csv(address, index_col='Date/Time')
# weather_2012_final['Temp (C)'].plot(figsize=(18, 6))

url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='latin1')
print(weather_mar2012)
