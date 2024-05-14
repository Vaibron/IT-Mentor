# Импорт библиотек pandas, matplotlib и numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Шаблон адреса для загрузки данных о погоде
url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"


# Функция для загрузки данных о погоде за определенный месяц и год
def download_weather_month(year, month):
    # Формирование адреса с использованием шаблона и подстановкой года и месяца
    url = url_template.format(year=year, month=month)
    # Чтение данных из CSV по URL, установка колонки 'Date/Time (LST)' как индекса и парсинг дат
    weather_data = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='utf-8-sig')
    # Удаление колонок с отсутствующими данными
    weather_data = weather_data.dropna(axis=1)
    # Удаление символов градуса из названий колонок
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    # Удаление ненужных колонок
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time (LST)', 'Longitude (x)',
                                      'Latitude (y)', 'Station Name', 'Climate ID'], axis=1)
    # Возвращение обработанных данных
    return weather_data


# Список данных о погоде за каждый месяц 2012 года
data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]
# Объединение данных за все месяцы в один DataFrame
weather_2012 = pd.concat(data_by_month)

# Путь к файлу для сохранения данных
address = '/Users/aleksejsypko/Desktop/Python/IT-Mentor/5. Потоки ввода-вывода/weather_2012.csv'
# Сохранение данных в CSV-файл
weather_2012.to_csv(address)

# Чтение сохраненных данных из CSV-файла
weather_2012_final = pd.read_csv(address, index_col='Date/Time (LST)')
# Визуализация данных о температуре
weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
# Отображение графика
plt.show()
