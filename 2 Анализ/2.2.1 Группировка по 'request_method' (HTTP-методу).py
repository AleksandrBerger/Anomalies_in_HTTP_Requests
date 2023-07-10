import pandas as pd


# Чтение файла CSV с помощью Pandas
df = pd.read_csv(r'D:\Тестовое задание\access.log\access_filtered.csv')


# Преобразование столбца 'status' в строковый тип данных
df['status'] = df['status'].astype(str)


# Фильтрация данных по столбцу "status" начинающемуся с цифры "3"
filtered_df = df[df['status'].str.startswith('3')]


# Выбор только нужных столбцов "request_method", "status", "datetime"
selected_df = filtered_df[['request_method', 'status', 'datetime']]


# Запись результата в файл CSV с помощью Pandas
selected_df.to_csv(r'D:\Тестовое задание\access.log\access_grouped_new.csv', index=False)
