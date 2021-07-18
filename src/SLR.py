#]here we will use scikit learn to calculate the regression that would be used to formulate the model
from sklearn.linear_model import LinearRegression#this imports the linear_model from scikit learn 

#SLR
#formular us y = bo + b1x where bo = intercept and b1= slope

#next we create a linear regression object using the constructor
lm = LinearRegression()

#then we define the predictor variable and target variable
x = df(["highway-mpg"])# #this is the predictor (independent) variable
y = (["price"]) #this is the target (dependent) variable

#we use the fit function to fit the model 
lm.fit(x, y) #to fine the parameters b0 and b1

#themn we use the predict predict to obtain a prediction 
yhat = lm.predict()

#to view the intercept b0 we use 
lm.intercept_

#to view the slope n1 we use 
lm.coef_

#the rekationship between price and highway MPG is given by
#price = lm.intercept_ + lm.coef_ * highwayMPG 