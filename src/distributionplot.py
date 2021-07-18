import seaborn as sns 

#to compare the fitted values to the actual values and see if our model is fit 
ax1 = sns.distplot(df['price'], hist = False, color = "r", label = "actual value")
#price is the actual value, we dont want an histogram so it is set to false, color is red and we set the label
sns.distplot(yhat, hist = False, color = "b", label = "fitted values", ax = ax1)
#this is the code fpr the plot of the predicted values 