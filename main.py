# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# Reading CSV files

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# PANDAS Library

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

average = (sum(temp_list) / len(temp_list))
print(average)

print(data["temp"].mean())

print(data["temp"].max())

# Get Data In Columns

print(data["condition"])

print(data.condition)

