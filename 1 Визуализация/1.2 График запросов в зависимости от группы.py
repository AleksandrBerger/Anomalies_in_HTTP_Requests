import pandas as pd
import matplotlib.pyplot as plt

output_file = r'D:\Тестовое задание\access.log\access_filtered.csv'

# Чтение только необходимых столбцов из файла CSV
usecols = ['datetime', 'status']
df = pd.read_csv(output_file, usecols=usecols)

# Преобразование столбца 'datetime' в формат даты и времени
df['datetime'] = pd.to_datetime(df['datetime'])

# Создание нового столбца 'status_group' на основе первой цифры статуса HTTP
df['status_group'] = df['status'].astype(str).str[0]

# Группировка по времени (по часам) и статусу, подсчет количества запросов
requests_per_hour_group = df.groupby([df['datetime'].dt.hour, 'status_group'])['status_group'].count()

# Построение графиков
groups = requests_per_hour_group.index.get_level_values('status_group').unique()

for group in groups:
    group_data = requests_per_hour_group.xs(group, level='status_group')
    plt.plot(group_data.index, group_data.values, label=f'Status Group {group}')

plt.xlabel('Hour of the day')
plt.ylabel('Number of requests')
plt.title('Requests per hour by Status Group')
plt.grid(True)
plt.legend()

# Изменение шкалы на оси Y
plt.ticklabel_format(style='plain')
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

plt.show()
