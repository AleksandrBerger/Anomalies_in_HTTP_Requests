import pandas as pd
import matplotlib.pyplot as plt


# Чтение файла CSV с помощью Pandas
df = pd.read_csv(r'D:\Тестовое задание\access.log\access_grouped_new.csv')


# Фильтрация данных по нужным методам запросов
filtered_df = df[df['request_method'].isin(['GET', 'HEAD', 'OPTIONS', 'POST'])]


# Преобразование столбца 'datetime' в тип данных datetime
filtered_df['datetime'] = pd.to_datetime(filtered_df['datetime'], errors='coerce')


# Удаление неверных значений в столбце 'datetime'
filtered_df = filtered_df.dropna(subset=['datetime'])


# Группировка данных по методам запросов и времени
grouped_df = filtered_df.groupby(['datetime', 'request_method']).size().unstack()


# Построение линейных графиков для каждого метода запроса
fig, ax = plt.subplots()


for method in ['GET', 'HEAD', 'OPTIONS', 'POST']:
   ax.plot(grouped_df.index, grouped_df[method], label=method)


# Настройка осей и заголовка
ax.set_xlabel('Datetime')
ax.set_ylabel('Number of Requests')
ax.set_title('Number of Requests by Request Method over Time')


# Легенда
ax.legend()


# Отображение графика
plt.show()
