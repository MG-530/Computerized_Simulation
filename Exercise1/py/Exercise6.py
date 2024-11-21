import numpy as np
import matplotlib.pyplot as plt
means = [1, 2, 3, 4, 5]  
std_dev = 1             
n = 1000                 
x_limits = (-2, 8)
y_limits = (0, 150)
for mean in means:
    data = np.random.normal(mean, std_dev, n) 
    plt.figure()
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(f'Normal Distribution Histogram (mean={mean}, std={std_dev})')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.xlim(x_limits)
    plt.ylim(y_limits)
    plt.grid(True)
    plt.savefig(f'Exercise6.{mean}.png', format='png', dpi=300)
    plt.show()
