import csv
import pandas as pd

# # Reading the uploaded CSV file and using .readlines() 
# # to create a list named data
# file_path = 'weather_data.csv'

# with open(file_path, 'r') as data_file:
#     data = data_file.readlines()

# # Displaying the first few lines of the data to confirm successful reading
# print(data)

# Opening and analyzing tabular data with csv library

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Using pandas library to do the same job.abs

data = pd.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])

#  Transforming a dataset into a dictionary

# data_dict = data.to_dict()
# print(data_dict)

# Transforming a column into a list

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
# average = sum(temp_list)/len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns

# print(data["condition"])   # threating data as a dictionary
# print(data.condition)        # threating data as an object (advanced way of doing things)

# ------ Get data in a row within a dataframe --------------- #

# print(data[data["day"] == "Monday"])
# max_temp_row = data.loc[data["temp"].idxmax()]  # Using pandas function
# print(max_temp_row)
# print(data[data.temp == data.temp.max()])       # Manually fetching

monday = data[data.day == "Monday"]
# print(monday.condition)
# Extracting Monday's temperature in Celsius
# monday_temp_celsius = weather_df.loc[weather_df['day'] == 'Monday', 'temp'].iloc[0]
monday_temp_celsius = monday.temp                # getting hold of monday temperature
# print(monday_temp_celsius)
# Converting to Fahrenheit
monday_temp_fahrenheit = (monday_temp_celsius * 9/5) + 32

# print(monday_temp_fahrenheit)

# Create a DataFrame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
df = pd.DataFrame(data_dict)
# print(df)
df.to_csv("students_data.csv")