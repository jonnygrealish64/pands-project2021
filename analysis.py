# This program involves the Fisher's Iris data set and outputs:
# 1. Summary of each variable to a single text file.
# 2. Histogram of each variable to png files.
# 3. Scatter plot of each pair of variables to png files.
# Author: Jonathon Grealish
# Reference Material:
# https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# https://stackoverflow.com/questions/43801152/read-output-of-a-csv-file-and-write-it-to-a-text-file-using-python
# https://stackoverflow.com/questions/49137535/converting-csv-to-txt-tab-delimited-and-iterate-over-files-in-directory-python
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib

import numpy as np # arrays tool
import pandas as pd # data analysis tool
import matplotlib.pyplot as plt # histogram and scatter plot tool
import csv

data = pd.read_csv("IRIS.csv") # this imports all data stored in the csv file

# Open file with "w" (write), the file will create automatically.
file = open("summary.txt", "w")
# Open csv file to read, using "with".
with open("IRIS.csv") as csvFile:
    readCsv = csv.reader(csvFile)
    for row in readCsv:
        # Manipulate all values in the file.write() using for loop to iterate through each row of data
        Id = row[0]
        Id1 = row[1]
        Id2 = row[2]
        Id3 = row[3]
        Id4 = row[4]
        # Format integers in data to strings.
        file.write(str(Id4) + "  " + str(Id3) + "  " + str(Id2) + "  " + str(Id1) + "  " + str(Id) + "  " + "\n")
# Close the file after writing to it.
file.close()

# For each histogram below:
# plt.figure(figsize = (x,y)) sets up the histogram's size.
# The variable x contains data related to an attribute from the csv file.
# plt.hist uses the data, bins (which divide the entire range into intervals) and colour.
# Titles for the histogram and axes are then added.
# The histogram is then saved using plt.savefig to a png file.

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

# For each scatter plot below:
# plt.figure(figsize = (x,y)) sets up the scatter plot's size.
# The variables x and y contains data related to attributes from the csv file.
# plt.scatter uses the data from the pair of variables and adds colour.
# Titles for the scatter plot and axes are then added.
# The scatter plot is then saved using plt.savefig to a png file.

# Scatter Plot for Sepal Length & Sepal Width:
plt.scatter(x = "sepal_length", y = "sepal_width", color = "purple")
plt.title("Sepal Length & Width Plot")
plt.xlabel("Sepal_Length")
plt.ylabel("Sepal_Width")

plt.savefig("IrisSepals.png")

# Scatter Plot for Petal Length & Petal Width:
plt.scatter(x = "petal_length", y = "petal_width", color = "purple")
plt.title("Petal Length & Width Plot")
plt.xlabel("Petal_Length")
plt.ylabel("Petal_Width")

plt.savefig("IrisPetals.png")