import pandas as pd

# Чтение файла CSV с помощью Pandas
df = pd.read_csv(r'D:\Тестовое задание\access.log\access_filtered.csv')

# Преобразование столбца 'datetime' в тип данных datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Применение фильтров
filtered_df = df[(df['status'] == 307) &
                 (df['datetime'].between('2022-11-23 18:00', '2022-11-23 19:00')) &
                 (df['request_method'] == 'GET')]

# Сохранение результатов в CSV
filtered_df.to_csv(r'D:\Тестовое задание\access.log\access_grouped_new3.csv', index=False)
