height = [1.70, 1.80, 1.65, 1,49]
weight = [65.0, 66.1, 56.7, 80.0]
import numpy as np 
np_height = np.array (height)# defining the lists as arrays to make calc faster and easier
np_weight = np.array (weight)
bmi = np_weight / np_height **2
bmi > 23#this will show all bmi greater than 23 as true else false 
bmi [bmi > 23]# subsetting: this shows all the values above 23
