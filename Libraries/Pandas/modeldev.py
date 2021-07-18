#MODEL DEVELOPMENT AND EVALUATION 
#We will try to predict the price of a car using our dataset. We will be using 
#1  Simple and multiple linear regression 
#2  Model Evaluation using visualizations 
#3  Polynomial regression and pipelines 
#4  R-squared and MSE for In-Sample evaluation 
#5  Prediction and Decision making 

#A model can be thought of as a mathematical equation used to predict a valuegiven one or more other values 
#The more relevant data ypu have, the more accurate your model is 

x = predictor variables 
y = target variable 
b0 = intercept 
b(1,2,3,4) = slope 

#SIMPLE LINEAR REGRESSION MODEL 
#Simple linear regression shows relationship between x and y  with the formula 
y = b0 + b1x 

#example -using nighway mpg to predict the price of a car 
x =  df]'highway-mpg']
y = df['price']

from skilearn.linear_model import LinearRegression 
SLmodel = LinearRegression()
SLmodel.fit (x, y)
Prediction = SLmodel.predict(x) #to obtain a prediction 
SLmodel.intercept_ #intercept
SLmodel.coef_ #slope 


#MULTIPLE LINEAR REGRESSION  MODEL 
##used to show the relationship between one or more predictor variables and a target variable 
#for example if we have 4 predictor variables the formular is 
#y = b0 + b1x1 +b2x2 + b3x3 + b4x4
#to trin the model 
x = df(['horsepower', 'curb-weight', 'engine-size', 'highway-mpg'])
y = df['price']
MLmodel = LinearRegression(x, y)
Results = MLmodel.predict(x)

#MODEL EVALUATION USING VISUALIZATION 
#Regression plot 
import seaborn as sns 
sns,regplot (x = "highway-mpg", y = "price", data = df)#Regression plot which is a scatter plot 
plt.ylim(0, )

#Residual plot 
#An evenly distributed linear plot accross the x axis implies that a linear model is suitable 
import seaborn as sns #seaborn is used to create a residual plot 
sns.residplot(df['highway-mpg'], df['price']) 

#Distribution plot 
# useful for visualising models with more than one independent variable or feature 
#It plots the predicted values against the actual values 
import seaborn as sns 
actual_values = sns.distplot (df['price'], hist = False, color = "r", label = "Actual Values")#plots distribution plot for the actual values 
sns.distplot(Results, hist = False, color = "b", label = "Fitted Values", ax = actual_values
#thi plots the fitted values against the actual values  on the actual_values axis 


#POLYNOMIAL REGRESSION MODEL 

#It is used when a linear model is not the best fit for our data 
#First we transform our data into a polynomial then we train/fit it with linear regression
#It is beneficial for describing curvilinear relationships 
#There are different orders, here we will look at second and third order 
#Quadratic (2nd order) - model = b0 + b1x1 + b2 (x1^2)
#Cubic (3rd order) - Model = b0 + b1x1 + b2(x1^2) + b3(x1^3)
#The degree of the order is important. Find the degree that fits your data well 

#One dimensional polynomial regression 
f = np.polyfit (x, y, 3) #3rd order polynomial regreesion 
p = np.poly1d(f) #to define the polynomial function 
print (p) #this prints the model formular for the polynomial regression  f 

#Polynomial regression models of multiple dimensions 
#the numpy polyfit function cannot handle this 
#we use the preprocessing library in scikit learn 
#POLYNOMIAL REGRESSION WITH MULTIPLE DIMENSIONS 
from skilearn.preprocessing import PolynomialFeatures 
pf = PolynomialFeatures (degree = 2)# to eefine the degree 
pf.fit_transform(1, 2 ), include_bias = False)# this transforms the data into polynimials. list all the variables

#We use the standardscalar in the preprocessing library as the dimensions increase  to standardize the values 
from skilearn.preprocessing import StandardScalar 
Scale = StandardScalar() #we train the object here 
Scale.fit (x_data [['horsepower', 'highway-mpg']])#this fits the object we created  >>>>>>Normlisation
x_scale = scale.fit(x_data [['horsepower', 'highway-mpg']]) # >>>>>>>Polynomial transform


#Pipelines - are used to simplify codes
#steps in getting a prediction are 
#Normlisation >>>>>>>>> Polynomial transform >>>>>>>> Linear regression 
from skilearn.linear_model import LinearRegression
from skilearn.preprocessing import StandardScalar
from skilearn.preprocessing import PolynomialFeatures
from skilearn.pipeline import Pipeline 

y = df['price'] #target variable 
input = [('scale', StandardScalar()), ('Polynomial', PolynomialFeatures(degree = 2)), ('mode', LinearRegression())
                     #Normalization >>>>>>>>>>>>>>>>>> Polynomial transform >>>>>>>>>>>>>> Linear regression 
#then we import the list into the pipeline constructor 
pipe = Pipeline(input)#we input it into the pipeline constructor object using the pipeline 
pipe.fit (df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y) #to fit or train the model 
#to obtain a prediction we use 
yhat = pipe.predict (x[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]) #used to obtain a prediction 


#IN SAMPLE EVALUATION
#used to determine how good our model fits numerically with our data 
# the important measures are - Mean squared error (MSE) and R-squared
#MSE 
from skilearn.metrics import mean_squared_error
mean_squared_error(df['price'[], yhat) #the actual value , the predicted value 

#R-squared ( coefficient of determination)
#to determine how close the data is to the fitted regression line 
#R^2 = 1 - MSE of regression line/ MSE of the avrerage of the data
#It mostly takes values between 0 and 1 . the value close to 1 implies the regression line performs well hence the model 
x = df['highway-mpg']
y = df['price']
SLmodel.fit(x, y)#here we train the model 
SLmodel.score(x, y) # this gives us the R-squared value 


#to get a prediction we fit the model first - example below 
SLmodel.fit (df['highway-mpg'], df['price'])# predictor variable, target variable 
yhat = SLmodel.predict (np.array[30.0].reshape(-1, 1)#this shows us the price of a car with higway mpg of 30 

#you can further authenticate the result by checking the coefficient 
SLmodel.coef_