#BINNING IS USED FOR GROUPING DATA 
#\Binning improves predictive models accuracy 
#NOTE THAT DATAFRAME = df 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

bins = np.linspace(min(["price"]), max(df["price"]), 4)# this creates 3 bins of equal width to categorise the data 
group_names = ("Low", "Medium", "High")#create the names for the bins created above 
df["binned_price"] = pd.cut(df["price"], bins, labels = group_names, include_lowest = True)
#then we can use histograms to visualise the bins we have created 
plt.hist(df["binned_price"], bins = 3)
plt.show()
#we have successfully binned the prices of the cars  
