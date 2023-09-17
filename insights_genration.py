import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from the text file and parse JSON-like entries
data_entries = []
with open("./data entry/received_data.txt", "r") as file:
    for line in file:
        entry = json.loads(line.strip())
        data_entries.append(entry)

# Create a DataFrame from the parsed data
data_df = pd.DataFrame(data_entries)

# Convert the "datetime" column to a datetime data type
data_df['datetime'] = pd.to_datetime(data_df['datetime'])

# Perform data analysis or calculations as needed
# For example, you can calculate summary statistics:
summary_stats = data_df.describe()

# Create time series plots for temperature and humidity
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='temp', data=data_df)
plt.title('Temperature Over Time')
plt.xlabel('Datetime')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='humi', data=data_df)
plt.title('Humidity Over Time')
plt.xlabel('Datetime')
plt.ylabel('Humidity')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# You can generate more insights and visualizations based on your specific analysis needs

# For example, you can calculate the average temperature and humidity:
average_temp = data_df['temp'].mean()
average_humidity = data_df['humi'].mean()

# Print the calculated values
print(f'Average Temperature: {average_temp}')
print(f'Average Humidity: {average_humidity}')
