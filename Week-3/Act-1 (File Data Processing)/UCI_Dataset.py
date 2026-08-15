# Pandas can make the code easier...
import pandas as pd
#pathlib can help in locating the file in much easier and protected way...
from pathlib import Path

file_path = Path(__file__).resolve().parent / "iris.data"

#Assigning the Column Headers for the Raw Data file
columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Flower Name"]

#Opens and separates CSV data into a Table
data = pd.read_csv(file_path,names= columns)

#Operations based on Activity...
count = len(data)                               #Counting the Number of Data
flower_names = data["Flower Name"].unique()     #Gets the Names of the Flower Name (without Repetition)
flower_count = data["Flower Name"].nunique()    #Gets the Number of Flowers, based on the Flower Name (without Repetition)

#Printing the Reqquired Info:
print(f"Total Number of Records: {count}")
print(f"Total Number of Flowers: {flower_count}")
print(f"Flower Names: {flower_names}")
