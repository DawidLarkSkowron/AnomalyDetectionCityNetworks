import pandas as pd
import matplotlib.pyplot as plt
# Load the data
file_path = 'DataSet\Dataset.csv'  # Update with your file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(data.head())



# Scatter plot for latitude vs longitude
plt.figure(figsize=(10, 6))
plt.scatter(data['longitude'], data['latitude'], alpha=0.5)
plt.title('City Locations on a Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

# Count the number of cities in each region
region_counts = data['region'].value_counts()

# Bar chart for regions
plt.figure(figsize=(12, 6))
region_counts.plot(kind='bar')
plt.title('Number of Cities by Region')
plt.xlabel('Region')
plt.ylabel('Number of Cities')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()