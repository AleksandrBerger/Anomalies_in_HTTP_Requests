import pandas as pd
import matplotlib.pyplot as plt


output_file = r'D:\Тестовое задание\access.log\output_full.csv'


# Чтение файла CSV и выбор необходимых столбцов
usecols = ['datetime', 'request_time']
df = pd.read_csv(output_file, usecols=usecols)


# Преобразование столбца 'datetime' в формат даты и времени
df['datetime'] = pd.to_datetime(df['datetime'])


# Установка столбца 'datetime' в качестве индекса
df.set_index('datetime', inplace=True)


# Агрегирование по 5-минутным периодам и вычисление среднего времени ответа
average_response_time = df['request_time'].resample('5T').mean()


# Построение графика
plt.plot(average_response_time.index, average_response_time.values)
plt.xlabel('Time')
plt.ylabel('Average Response Time (seconds)')
plt.title('Average Response Time per 5-minute Period')
plt.grid(True)
plt.show()
