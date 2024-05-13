import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/weather_2012.csv'

weather_2012_final = pd.read_csv(address, index_col='Date/Time (LST)')
weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
plt.show()
