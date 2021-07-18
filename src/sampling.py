import numpy as np 
height = np.round (np.random.normal (1.82, 0.30, 5000), 2)
weight = np.round (np.random.normal (70.2, 15.0, 5000), 2)
np_city = np.column_stack(height, weight)