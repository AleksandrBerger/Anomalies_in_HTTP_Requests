import pandas as pd
import matplotlib.pyplot as plt

output_file = r'D:\Тестовое задание\access.log\access_filtered.csv'

# Чтение только необходимых столбцов из файла CSV
usecols = ['datetime']
df = pd.read_csv(output_file, usecols=usecols)

# Преобразование столбца 'datetime' в формат даты и времени
df['datetime'] = pd.to_datetime(df['datetime'])

# Группировка по времени (по часам) и подсчет количества запросов
requests_per_hour = df.groupby(df['datetime'].dt.hour)['datetime'].count()

# Построение графика
plt.plot(requests_per_hour.index, requests_per_hour.values)
plt.xlabel('Hour of the day')
plt.ylabel('Number of requests')
plt.title('Requests per hour')
plt.grid(True)

# Изменение шкалы на графике
plt.ticklabel_format(style='plain')

plt.show()
