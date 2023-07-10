import pandas as pd
import matplotlib.pyplot as plt


# Чтение файла CSV с помощью Pandas
df = pd.read_csv(r'D:\Тестовое задание\access.log\access_grouped_new2.csv')


# Преобразование столбца 'datetime' в тип данных datetime
df['datetime'] = pd.to_datetime(df['datetime'])


# Фильтрация данных по статусам 301, 302 и 307
status_301 = df[df['status'] == 301]
status_302 = df[df['status'] == 302]
status_307 = df[df['status'] == 307]


# Группировка данных и подсчет количества запросов для каждого статуса
grouped_301 = status_301.groupby('datetime').size()
grouped_302 = status_302.groupby('datetime').size()
grouped_307 = status_307.groupby('datetime').size()


# Построение линейного графика для каждого статуса
fig, ax = plt.subplots()
ax.plot(grouped_301.index, grouped_301.values, label='301')
ax.plot(grouped_302.index, grouped_302.values, label='302')
ax.plot(grouped_307.index, grouped_307.values, label='307')


# Настройка осей и заголовка
ax.set_xlabel('Datetime')
ax.set_ylabel('Number of Requests')
ax.set_title('Number of Requests for Status 301, 302, 307 over Time')


# Добавление легенды
ax.legend()


# Отображение графика
plt.show()
