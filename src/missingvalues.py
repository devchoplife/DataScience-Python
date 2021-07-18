#we usually perform operations along columns
import pandas as pd 
df("symboling")#this references the symboling column 
df("symboling") = df("symboling") + 1 #this adds 1 to the current value of the symboling column 

#Dealing with missing values
df.dropna(subset = ["price"], axis = 0, inplace = True)#drops the entire missing value row axis =1 for column  
#or 
df = df.dropna(subset = ["price"], axis = 0)#also frops the entire missing value row

#replace missing values NaN 
#if youre replacing it with the mean py will calc the mean first 
mean = df["normalised losses"].mean()#to calculate the mean of all the entires 
df["normalised losses"].replace(np.nan, mean)#np.nan is the error that was shown. its a numpy error being a numeric data
#or 
df.replace(np.nan, mean)

#to access the column body style  
df["body-style"]