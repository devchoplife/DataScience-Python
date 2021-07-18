import matplotlib.pyplot as plt 

values = [0, 0.6, 0.8, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 3.4, 2.6]

plt.hist (values, bin = 3)#plots a three column histogram
plt.show ()#display the histogram