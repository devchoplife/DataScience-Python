height = [1.70, 1.80, 1.65, 1,49]
weight = [65.0, 66.1, 56.7, 80.0]
import numpy as np 
np_2d = np.array ([[1.70, 1.80, 1.65, 1,49],
                 [65.0, 66.1, 56.7, 80.0]]) #this is a 2 dimensional numpy array 
np_2d.shape #shows the number of rows and columns available in the numpy array
np_2d [0]# shows the first row 
np_2d [0][2] # output will be the 1.80 which is in the second column in the first row
np_2d [0, 2]# This is another way of getting values from the arrayin the prder rpw, column
np_2d [:,0:3]#this will show from the first column to to the thir column and exclude the last one 
np_2d [1, :]#this shows the entire weight row 
   