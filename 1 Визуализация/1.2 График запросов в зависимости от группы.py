import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

output_file = r'D:\Тестовое задание\access.log\access_filtered.csv'

# Read only necessary columns from the CSV file
usecols = ['datetime', 'status']
df = pd.read_csv(output_file, usecols=usecols)

# Convert 'datetime' column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Create a new column 'status_group' based on the first digit of the HTTP status
df['status_group'] = df['status'].astype(str).str[0]

# Filter data for specific status groups
status_to_plot = ['2', '3', '4', '5']
df_filtered = df[df['status_group'].isin(status_to_plot)]

# Group by time (in 15-minute intervals) and status, count the number of requests
requests_per_hour_group = df_filtered.groupby([pd.Grouper(key='datetime', freq='15Min'), 'status_group'])['status_group'].count()

# Plotting
groups = requests_per_hour_group.index.get_level_values('status_group').unique()

for group in groups:
    group_data = requests_per_hour_group.xs(group, level='status_group')
    plt.plot(group_data.index, group_data.values, label=f'Status Group {group}')

plt.xlabel('Time')
plt.ylabel('Number of requests')
plt.title('Requests per hour by Status Group')
plt.grid(True)
plt.legend()

# Adjust the x-axis ticks
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.show()