import pandas as pd
import matplotlib.pyplot as plt

output_file = r'D:\Тестовое задание\access.log\access_filtered.csv'

# Чтение только необходимых столбцов из файла CSV
usecols = ['datetime']
df = pd.read_csv(output_file, usecols=usecols)

# Преобразование столбца 'datetime' в формат даты и времени
df['datetime'] = pd.to_datetime(df['datetime'])

# Группировка по времени с шагом в 10 минут и подсчет количества запросов
requests_per_10_minutes = df.groupby(pd.Grouper(key='datetime', freq='10T')).size()

# Построение графика
plt.plot(requests_per_10_minutes.index, requests_per_10_minutes.values)
plt.xlabel('Time')
plt.ylabel('Number of requests')
plt.title('Requests per 10 minutes')
plt.grid(True)

plt.show()
