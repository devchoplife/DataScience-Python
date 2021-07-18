#TO FIT/TRAIN A MODEL IN PYTHON QWE USE SCIKIT-LEARN 
#First import linear model from scikit learn 
from sklearn.linear_model import LinearRegression 
SLR = LinearRegression()#we define x and y before inputin it here ie predictor and target variables
SLR.fit(x, y)#predictor and target variables 
Result = SLR.predict(x) # to obtain a prediction  from the model 
SLR.intercept_ #to get the intercept of the model 
SLR.coef_ # to get the slope of the model 

#POLYNOMIAL REGRESSION WITH MULTIPLE DIMENSIONS 
from sklearn.preprocessing import PolynomialFeatures 
pf = PolynomialFeatures (degree = 2)# to eefine the degree 
pf.fit_transform(1, 2 ), include_bias = False)# this transforms the data into polynimials. list all the variables 

#when th dimensions become larger we use the standard scalar to fit the model 
from sklearn.preprocessing import StandardScalar 
Scale = StandardScalar() #we train the object here 
Scale.fit (x_data [['horsepower', 'highway-mpg']])#this fits the object we created 
x_scale = scale.fit(x_data [['horsepower', 'highway-mpg']])#transforms the data into a new dataframe 

#MEAN SQUARED ERROR 
from sklearn import mean_squared_error 
mean_squared_error(actual_value, predicted_value)

#SPLITTING DATA INTO TRAINING AND TESTING SET 
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x_data, y_data, test_size = 0.3, random_state = 0)
#test_size is the percentage of data for testing which is 30 percent here 
#random_state is a  number generator used for random sampling 

#CROSS VALIDATION SCORE 
from sklearn.model_selection import cross_val_score 
cvs = cross_val_score(lr, x_data, y_data, cv = 3)#type of model, predictor, target, no of folds  or partitions 
#the model would have been created before using the object here
cross_val_predict(lr, x_data, y_data, cv = 3) # returns the prediction for each element when it was i the test set 

#RIDGE REGRESSION FOR CONTROLLING ALPHA VALUES AND OVERFITTING 
from sklearn.linear_model import Ridge 
Ridgemodel = Ridge(alpha = 0.1) #create a ridge object using the constructor with aplha value 
Ridgemodel.fit (x, y) #refit/retrain the ridge model 
yhat= Ridgemodel,predict(x) #to obtain a prediction 
