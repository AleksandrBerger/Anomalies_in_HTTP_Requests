import pandas as pd

chunk_size = 10000  # Размер чанка (количество строк для чтения за один раз)
filtered_df = pd.DataFrame()  # Пустой DataFrame для сохранения результатов

# Чтение файла по частям
for chunk in pd.read_csv(r'D:\Тестовое задание\access.log\access_filtered.csv', chunksize=chunk_size):
    filtered_chunk = chunk[(chunk['status'] == 307) &
                           (chunk['request_method'] == 'GET') &
                           (chunk['remote_addr'] == '77.51.117.176')]
    filtered_df = pd.concat([filtered_df, filtered_chunk])

row_count = len(filtered_df)
