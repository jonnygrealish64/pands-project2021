# This program involves the Fisher's Iris data set and outputs the following:
# 1. Summary of each variable to a txt file.
# 2. Histogram of each variable to png files.
# 3. Scatter plot of each pair of variables to png files.
# Author: Jonathon Grealish
# Reference Material:
# https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# https://stackoverflow.com/questions/43801152/read-output-of-a-csv-file-and-write-it-to-a-text-file-using-python
# https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib

import numpy as np # arrays tool
import pandas as pd # data analysis tool
import matplotlib.pyplot as plt # histogram tool
import seaborn # scatter plot tool
import csv # csv tool

data = pd.read_csv("IRIS.csv") # this imports all data stored in the csv file.

# 1. Summary of each variable to a txt file:
# To convert csv to txt:
# Open text file with "w" (write), creating the file.
# Open csv file to read, using "with" as.
# Manipulate all values in the file.write() using a for loop to iterate through each row of data.
# Format all integers in data to strings, with spacing in between each column of values.
# Close the file after writing to it.
file = open("summary.txt", "w")
with open("IRIS.csv") as csvFile:
    readCsv = csv.reader(csvFile)
    for row in readCsv:
        Id = row[0]
        Id1 = row[1]
        Id2 = row[2]
        Id3 = row[3]
        Id4 = row[4]
        file.write(str(Id4) + "  " + str(Id3) + "  " + str(Id2) + "  " + str(Id1) + "  " + str(Id) + "  " + "\n")
file.close()

# 2. Histogram of each variable to png files:
# For each histogram below:
# plt.figure(figsize = (10,7)) sets up the histogram's size.
# The variable x contains data related to an attribute from the csv file.
# plt.hist uses the data, bins (which divide the entire range into intervals) and colour.
# Titles for the histogram and axes are then added.
# The histogram is then saved using plt.savefig() to a png file.

# Histogram for Sepal Length:
plt.figure(figsize = (10, 7))
x = data["sepal_length"]

plt.hist(x, bins = 20, color = "purple")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

plt.savefig("IrisSepalLength.png")

# Histogram for Sepal Width:
plt.figure(figsize = (10, 7))
x = data["sepal_width"]
  
plt.hist(x, bins = 20, color = "purple")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")

plt.savefig("IrisSepalWidth.png")

# Histogram for Petal Length:
plt.figure(figsize = (10, 7))
x = data["petal_length"]
  
plt.hist(x, bins = 20, color = "purple")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")

plt.savefig("IrisPetalLength.png")

# Histogram for Petal Width:
plt.figure(figsize = (10, 7))
x = data["petal_width"]
  
plt.hist(x, bins = 20, color = "purple")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")

plt.savefig("IrisPetalWidth.png")

# 3. Scatter plot of each pair of variables to png files:
# For each scatter plot below:
# Titles of the pair of attributes are established on the axes.
# The attributes are plotted via data.plot(kind, x, y, c), using attribute values from the csv file.
# The scatter plot is then saved using plt.savefig() to a png file.

# Scatter Plot for Sepal Length & Sepal Width:
plt.title("Sepal Length & Width Plot")
plt.xlabel("Sepal_Length")
plt.ylabel("Sepal_Width")

data.plot(kind = "scatter", x = ["sepal_length"], y = ["sepal_width"], color = "purple")
plt.savefig("IrisSepals.png")

# Scatter Plot for Petal Length & Petal Width:
plt.title("Petal Length & Width Plot")
plt.xlabel("Petal_Length")
plt.ylabel("Petal_Width")

data.plot(kind = "scatter", x = ["petal_length"], y = ["petal_width"], color = "yellow")
plt.savefig("IrisPetals.png")