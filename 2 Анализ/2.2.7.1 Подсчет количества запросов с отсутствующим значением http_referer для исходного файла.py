import pandas as pd

# Чтение файла CSV с помощью Pandas
df = pd.read_csv(r'D:\Тестовое задание\access.log\access_filtered.csv')

# Преобразование столбца 'datetime' в тип данных datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Применение фильтров
filtered_df = df[(df['status'] == 307) &
                 (df['request_method'] == 'GET') &
                 (df['http_referer'] == '-')]

# Подсчет количества строк
row_count = len(filtered_df)

# Вывод результата
print("Количество строк с http_referer равным '-':", row_count)
