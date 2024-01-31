# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:25:54 2024

@author: Janica van Wyk
"""

"""
2. Extract, Transfrom, Load
2.1 Extract
"""

import pandas as pd

# Different file locations

df1 = pd.read_csv("data_02/country_data_index.csv")                  # Files in a different file location

"""
Absolute path:
D:/Universiteit/Coding Summer School/Week 1/2/CSS2024_Day02/data_02/country_data_index.csv

Relative path:
data_02/country_data_index.csv
"""


df2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")    # File from an URL

# Add header info for columns

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None, names=column_names)

url = "https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv"

df2 = pd.read_csv(url, header=None, names=column_names)

# Different file types

df3 = pd.read_csv("data_02/Geospatial Data.txt", sep=";")            # Text file with ;

df4 = pd.read_excel("data_02/residentdoctors.xlsx")                  # Excel

df5 = pd.read_json("data_02/student_data.json")                      # Json

# Misc

url2 = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

df6 = pd.read_csv(url2)

# print(df6.info())
# print(df6.describe())

# df = pd.read_csv("chat_files/Acceerometer_data.csv", names = ["date_time", "x", "y", "z"])

# df = pd.read_json("")


"""
2.2 Transform
"""

# Index column

df7 = pd.read_csv("data_02/country_data_index.csv", index_col=0)

# Skip rows

df8 = pd.read_csv("data_02/insurance_data.csv", skiprows=5)

# Column heading

column_names2 = ["duration", "pulse", "max_pulse", "calories"]

df9 = pd.read_csv("data_02/patient_data.csv", header=None, names=column_names2)

# Unique delimiter

df10 = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

# Incosistent data types and names

df11 = pd.read_excel("data_02/residentdoctors.xlsx")

print(df11.info())

# Create new column: convert age range to column with just lower value

df11["LOWER_AGE"] = df11["AGEDIST"].str.extract('(\d+)-')
df11["UPPER_AGE"] = df11["AGEDIST"].str.extract('-(\d+)')

# Convert to int

df11['LOWER_AGE'] = df11['LOWER_AGE'].astype(int)

print(df11.info())

"""
Regular expressions

df11["LOWER_AGE"] = df11["AGEDIST"].str.extract('(\d+)-')

\d : refers to any digit
+ : can be multiple digits
- : followed by a hyphen

"""


""" Working with dates

10-01-2024 - UK

01-10-2024 - US

"""

df12 = pd.read_csv("data_02/time_series_data.csv", index_col=0)

print(df12.info())

df12['Date'] = pd.to_datetime(df12['Date'], format="%Y-%m-%d")

print(df12.info())

# Split into separate columns

df12['Year'] = df12['Date'].dt.year

df12['Month'] = df12['Date'].dt.month

df12['Day'] = df12['Date'].dt.day

"""
.str
.extract
.astype
"""

############################################################################

"""
NANs and Wrong Formats
"""

df = pd.read_csv("data_02/patient_data_dates.csv")

# See all rows

pd.set_option('display.max_rows',None)

print(df)

# Remove index column (or any other)

df.drop(['Index'],inplace=True,axis=1)

# Replace Empty Values - Using fillna

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

# Wrong Date Format – Convert with to_datetime()

df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# Removing Empty Cells – Using dropna

df.dropna(subset=['Date'], inplace = True)             # Drop rows in Data with Na lines

df = df.reset_index(drop=True)                         # Make row numbers consequtive

"""
df.dropna(inplace = True) - Drop all rows with Na

df.drop(index=26, inplace=True) - Or drop a row like this
"""

# Wrong Data – Replace and Remove Rows

df.loc[7, "Duration"] = 45

# df['Duration'] = df['Duration'].replace([450],50)

# Removing Duplicates – Using drop_duplicates()

df.drop_duplicates(inplace=True)

df = df.reset_index(drop=True)

print(df)

print("\n")


""" MEMO..... NANs and Wrong Formats

df = pd.read_csv('data_02/patient_data_dates.csv')

pd.set_option('display.max_rows',None)

print(df)

# Drop Index Column:

df.drop(['Index'],inplace=True,axis=1)

print(df)

# Fill NaNs or empty fields in Calorie Column

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df)

# Convert Wrong Date Format in Date Column

df['Date'] = pd.to_datetime(df['Date'])

# Drop NaT field in Date Column

df.dropna(subset=['Date'], inplace = True)

print(df)

# Remove any rows that have NaNs or empty fields
# Here only the row 1 for the MaxPulse column as the rest have been resolved
df.dropna(inplace = True)

# Reset index
df = df.reset_index(drop=True)

print(df)

# Remove duplicates found in line 10 and 11
df.drop_duplicates(inplace = True)

df = df.reset_index(drop=True)

print(df)
"""
############################################################################

"""
Applying Data Transformations
"""

# Aggregation

df = pd.read_csv("data_02/iris.csv")

col_names = df.columns.tolist()

print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2
df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2)      # More appropiate for more complex calculations

grouped = df.groupby('class')

# Calculate mean, sum, and count for the squared values

mean_squared_values = grouped['sepal_length_sq'].mean()

sum_squared_values = grouped['sepal_length_sq'].sum()

count_squared_values = grouped['sepal_length_sq'].count()

print("Mean of Sepal Length Squared:")
print(mean_squared_values)
print("\nSum of Sepal Length Squared:")
print(sum_squared_values)
print("\nCount of Sepal Length Squared:")
print(count_squared_values)


# Append & Merge

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")


# Concatenate the dataframes
df = pd.concat([df1,df2], ignore_index=True)
# of... df = df.reset_index(drop=True)

# Merge based on one related column, i.e., ID

df1 = pd.read_csv("data_02/person_education.csv")
df2 = pd.read_csv("data_02/person_work.csv")

df_merge_inner = pd.merge(df1, df2, on='id')                    # merge only where both has the ID

df_merge_outer = pd.merge(df1, df2, on='id', how='outer')       # merge everything



# Filtering

df = pd.read_csv("data_02/iris.csv")

df["class"] = df["class"].str.replace("Iris-", "")

df = df[df['sepal_length'] > 5]

df = df[df['class'] == "virginica"]


"""
# Filter data for females (class == 'Iris-versicolor')

iris_versicolor = df[df['class'] == 'Iris-versicolor']

# Calculate the average iris_versicolor_sep_length

avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean() """


# Export data

df.to_csv("data_02/output/iris_data_cleaned.csv")
df.to_csv("data_02/output/iris_data_cleaned.csv", index=False)

df.to_excel("data_02/output/iris_data_cleaned.xlsx", index=False, sheet_name='Sheet1')

df.to_json("data_02/output/iris_data_cleaned.json", orient='records')

