import pandas as pd 

#there are three ways of normalizing data
#The first on is feature scaling method 
df["length"] = df["length"]/df["length"].max() #formula is = old value/maximum value

#second is min max mehod 
#formula = old - minimum/ maximum -minimum
df["lenght"] = (df["length"] - df["length"].min())/
															(df["length"].max() - df["length"].min())
															
#the last one is the z score method 
#formula = old - mean / standard devaition
df["length"] = (df["length"] - df["length".mean())/df["length"].std()]