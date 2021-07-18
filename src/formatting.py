import pandas as pd 

#to do calculations 
#say we want to covert a column from mpg to L/100km
df["city-mpg"] = 235/df["city-mpg"]# this calculates it in litres per 100 kilometer 

#then rename the column to litres per 100 kilomete
df.rename(columns =("city-mpg" : "city- L/100km"), inplace = True)#this renames the column or 

#to convert datatypes
df["price"] = df ["price"].astype["int"]#changes the data type to integer 