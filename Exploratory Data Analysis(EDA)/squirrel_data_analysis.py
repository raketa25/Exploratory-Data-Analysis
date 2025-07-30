import pandas as pd

# Importing data

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
missing_values = data.isnull().sum()   # Missing values per column
# print(missing_values)

# data_copy = data.copy()
# print(data_copy)

# Getting hold of the number of different squirrel color

squirrel_colors = data["Primary Fur Color"]
# print(squirrel_colors)
nbr_colors = squirrel_colors.unique()
# print(nbr_colors)

# ------- Extraction of squirrels by colors ---------

gray_squirrels = data[squirrel_colors == "Gray"]
# print(gray_squirrels)

cinnamon_squirrels = data[squirrel_colors == "Cinnamon"]
# print(cinnamon_squirrels)

black_squirrels = data[squirrel_colors == "Black"]
# print(black_squirrels)

gray_squirrels_count = len(gray_squirrels)
print(gray_squirrels_count)

cinnamon_squirrels_count = len(cinnamon_squirrels)
print(cinnamon_squirrels_count)

black_squirrels_count = len(black_squirrels)
print(black_squirrels_count)

# Creation of a small dataset of squirrels by number of colors

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("Squirrels_count.csv")
