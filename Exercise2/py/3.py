import numpy as np
import matplotlib.pyplot as plt
# Define the LCG parameters
m = 2**31 - 1  # Modulus 
a = 1103515245  # Multiplier
c = 12345       # Increment
seed = 0       
n = 10000
def lcg(seed, a, c, m, n):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x / m)
    return np.array(numbers)
lcg_numbers = lcg(seed, a, c, m, n)
lcg_mapped = lcg_numbers * (23 - (-10)) - 10
randint_numbers = np.random.uniform(-10, 23, n)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(lcg_mapped, bins=30, color='blue', alpha=0.7, label='LCG')
plt.title('Histogram of LCG Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.subplot(1, 2, 2)
plt.hist(randint_numbers, bins=30, color='green', alpha=0.7, label='Python randint')
plt.title('Histogram of Python randint Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()
