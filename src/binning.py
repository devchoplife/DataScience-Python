#binning means grouping values into bins e.g age groups
import numpy as np 
import pandas as pd 

bind = np.linspace (min(df["price"]), max (df["price"], 4)#the 4 reps the length of numbers to bin 
group_names = ["Low", "Medium", "High"]#this willl be used to label the bins 
df["price-binned"] = pd.cut(df["price"], bins, labels = group_names, include_lowest = True)
#the above code will label the prices as low, medium and high 


#to conert categorical var into numeric var for statistical models we us one-hot encodin
#te.g if fuel is set to gas and diesel and we apply this encoding 
#any car that has gas as fuel sets gas as fuel and diesel as o and vice versa
pd.get_dummies(df["fuel"])