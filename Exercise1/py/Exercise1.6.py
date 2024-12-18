import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0) 
x = np.random.normal(loc=100, scale=10, size=50)
y = np.random.normal(loc=300, scale=15, size=50)
z = np.random.normal(loc=40, scale=8, size=50)  
w = (x + y) / z
plt.hist(w, bins=np.arange(min(w), max(w) + 3, 3), edgecolor='black')
plt.title('Histogram of w = (x + y) / z')
plt.xlabel('Value of w')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()