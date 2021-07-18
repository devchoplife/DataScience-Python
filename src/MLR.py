#if we have 4 predictor variables 
#let us extract the four predictor variables and store them in a variable z 
from sklearn.linear_model import LinearRegression
#formular  is y = b0 + b1x1 + b2x2 + b3x3 + b4x4
lm = LinearRegression
z = (['horsepower', 'curb-weight', 'engine-size', 'highway-mpg'])

#then fit the variables into the model remembering to add the target variable 
lm.fit (z, df['price'])
 
#we can also get a prediction by using the predict method 
yhat = lm.predict(x)#this will show the arrays with column heading x1 to x4 

#then we calculate the intercept and coefficient

lm.intercept_
lm.coef_
#the formular should be clear from the process already 