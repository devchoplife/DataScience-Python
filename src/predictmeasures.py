#to make a prediction 
#for example to predicts a car price based on highway mpg

lm.fit(df["highway-mpg"], df["price"])#first we train the model 
lm.predict(np.array(30.0).reshape(-1, 1))#to find the price of a car with highway mpg of 30

#we can check how correct it is by using the 
lm.coef_

#to predict the values of highqay mpg from 1 to 100 
import numpy as np
new_input = np.arange(1, 101, 1).reshape(-1, 1)
#the parameters for the arange function are the start number, the end number plus 1 and the step size between elements
yhat = lm.predict (new_input)
#use a regression plot to visualize your results to see how correct the model is 
#then proceed to the residual plot
#then a distribution plot 
#then move to the mean square error whic is the most effectve method 
#r squared is anothe method to evaluate your model 
