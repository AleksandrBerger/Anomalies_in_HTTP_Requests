import pandas as pd
import matplotlib.pyplot as plt

# Чтение файла CSV с помощью Pandas
df = pd.read_csv(r'C:\Users\Berge\Downloads\access_grouped_new3_202307111624.csv')

# Преобразование столбца 'datetime' в тип данных datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Подсчет количества запросов для каждого временного интервала
requests_count = df.groupby('datetime').size()

# Построение линейного графика
plt.plot(requests_count.index, requests_count.values)

# Настройка осей и меток
plt.xlabel('Дата и время')
plt.ylabel('Количество запросов')
plt.title('Линейный график количества запросов по времени без remote_addr = "77.51.117.176"')

# Отображение графика
plt.show()
