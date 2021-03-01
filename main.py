# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# Reading CSV files

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# PANDAS Library

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(len(temp_list))

# average = (sum(temp_list) / len(temp_list))
# print(average)

# print(data["temp"].mean())

# print(data["temp"].max())

# Get Data In Columns

# print(data["condition"])

# print(data.condition)

# Get Data In Row...

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create A Data Frame From Scratch...

# data_dictionary = {
#     "students": ["Abhay", "Bhaskar", "Chandra"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dictionary)
# data.to_csv("new_data_dict.csv")

import pandas

data = pandas.read_csv("Squirrel_Data_2018.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("squirrel_count.csv")

