import numpy as np # arrays tool
import pandas as pd # data analysis tool
import matplotlib.pyplot as plt # histogram and scatter plot tool

# Scatter Plot for Sepal Length & Sepal Width:
plt.scatter(x = "sepal_length", y = "sepal_width", color = "purple")
plt.title("Sepal Length & Width Plot")
plt.xlabel("Sepal_Length")
plt.ylabel("Sepal_Width")

plt.savefig("IrisSepals.png")

# Scatter Plot for Petal Length & Petal Width:
plt.scatter(x = ["petal_length"], y = ["petal_width"], color = "purple")
plt.title("Petal Length & Width Plot")
plt.xlabel("Petal_Length")
plt.ylabel("Petal_Width")

plt.savefig("IrisPetals.png")