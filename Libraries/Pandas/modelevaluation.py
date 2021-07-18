#DIFFERENT WAYS OF EVALUATING A MODEL 
#It tells us how our model perform in the real world 
#In--sample evaluation shows  how well our model works with trained data but dosent tell us how well it can predict new  data 
#The solution is to split the data into two ; training and testing set 
#then test how it works in the real world
#the larger portion of data is used for training 
#the smaller portion is used for testing 
#after testing the model use all the data to train the model for full performance 
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(df['highway-mpg'],df['price'], test_size = 0.3, random_state = 0)
#test_size is the percentage of data for testing which is 30 percent here 
#random_state is a  number generator used for random sampling 
#x_train and y_train are the training sets white x_test and y_test are the testing sets 

#GENERALISATION PERFORMANCE 
#Generalisation error is a measure of how well our model does at predicti9ong previously unseen data 

#CROSS VALIDATION 
#the data set is seperated into different folds. then we use some part for training set and the rest for testing 
from sklearn.model_selection import cross_val_score 
scores = cross_val_score(SLmodel, df['highway-mpg'], df['price'], cv = 3)
#then we look for the mean to get the r square  value 
np.mean(scores)
cross_val_predict(SLmodel, df['highway-mpg'], df['price'], cv = 3)

#OVERFITTING, UNDERFITTING AND MODEL SELECTION 
#here we see how to pichk the best polynomial order for our model 
#UNDERFITTING : when the model is too simple to fit the data 
#OVERFITTING: when the model is too flexible and fits the noise rather than the function 
#use plots to evalueate different models ie r square, mse, train_test_split, cross  etc 
#plot the order of polynomial on the x axis and the mse on the y axis for the train andtest set to see which model has hhe least error 
#plot agianst r squared 

#How to calcu;ate r squared for differnt polynomial orders 
Rsqu_test = []
order = [1, 2, 3, 4} #the orders we want to calculate for 
for n in order: #this assigns all the values to n 
    pr = PolynomialFeatures(degree = n) #create a polynomial feature object 
    x_train_pr = pr.fit_transform (x_train[['horsepower']])
    x_test_pr = pr.fit_transform (x_test[['horsepower']]#we transform the traiin and test data into a polynomial  
    lr = LinearRegression()
    lr.fit (x_train_pr, y_train)#we fit the regression model using the transformed data 
    lr.fit (x_test_pr, y_test)
Rsqu_test.append(lr.score(x_test_pr, y_test))

#RIDGE REGRESSION 
#It prevents overfitting 
#Overfitting is a problem when we have multiple independent variables or features 
#we will focus on polynomial regression here 
#it controls the magnitude of the polynomial coefficient by introducing the parameter alpha 
#alpha is a parameter we select before fitting/training the model 
#we use cross validation to select alpha 

from sklearn.linear_model import Ridge 
Ridgemodel = Ridge(alpha = 0.1) #create a ridge object using the constructor with aplha value 
Ridgemodel.fit (x, y) #refit/retrain the ridge model 
yhat= Ridgemodel,predict(x) #to obtain a prediction 

#to determine the alpha value we use some data set for training and the other is called validation data, similar to test data
#the validation data is used to select parameters like alpha 
#we look for the r square of each alpha value and use visualisatin to check which is the best fit 


#GRID SEARCH 
#it allows us to search through multiple free parameters using few lines of code 
#it takes the model you would like to train and and different values of the hyper parameters 
#it them calculates the MSE or r square values for various hyper parameters value 
#allowing you to choose the best values 
#to select the hyper parameters we split our data into 3 sets 
#train, validation and test 
parameters = ({'Alpha':[1, 10, 100, 1000]}) #value of grid search is a pythoon list with a python dictionary 
#the key is the ma,e of the free parameter and the values are the parameter values 
from sklearn.linear_model import Ridge 
from sklearn.model_selection import GrisSearchCV
parameters1 = ({'Alpha':[0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 10000000]}) 
RR = Ridge()
Grid1 = GrisSearchCV(RR, parameters1, cv = 4)
#the inputs of the gridsearchcv object are the ridge regression objects and the number of folds 
Grid1.fit (x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg'[[, y_data)
Grid1.best_estimator_#finds the best values for the free parameters 

scores = Grid1.cv_results_# caculates the mean test score 
scores['mean_test_score']

#the advantage of grid search is how quickly we can test multiple parameters 