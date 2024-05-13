import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'


address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/weather_2012.csv'

weather_2012 = pd.read_csv(address, parse_dates=True, index_col='Date/Time (LST)')
#print(weather_2012[:5])

weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')

# Код сначала преобразует булевы значения в столбце is_snowing в числа, а затем строит график, который показывает, когда шел снег
is_snowing2 = is_snowing.astype(int)
is_snowing2.plot()
# Выводи график
plt.show()

weather_2012['Temp (C)'].resample('ME').median().plot(kind='bar') # Используйте 'ME' вместо 'M' для получения медианы температуры в конце каждого месяца
# Выводи график
plt.show()

print(is_snowing.astype(int)[:10])

print(is_snowing.astype(int).resample('ME').mean())


is_snowing.astype(int).resample('ME').mean().plot(kind='bar')
# Выводи график
plt.show()


temperature = weather_2012['Temp (C)'].resample('ME').median()
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(int).resample('ME').mean()

# Name the columns
temperature.name = "Temperature"
snowiness.name = "Snowiness"
stats = pd.concat([temperature, snowiness], axis=1)
print(stats)
stats.plot(kind='bar')
plt.show()

stats.plot(kind='bar', subplots=True, figsize=(15, 10))
plt.show()


