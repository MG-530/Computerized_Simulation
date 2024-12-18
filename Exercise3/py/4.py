import numpy as np
import matplotlib.pyplot as plt

def triangular_distribution_function(x, a, b, c):
    return np.where((a <= x) & (x < c), 2 * (x - a) / ((b - a) * (c - a)),
           np.where((c <= x) & (x <= b), 2 * (b - x) / ((b - a) * (b - c)), 0))

def accept_reject_sampling(target_func, domain, n_samples, max_val, *params):
    samples = []
    x_min, x_max = domain
    while len(samples) < n_samples:
        x = np.random.uniform(x_min, x_max)
        u = np.random.uniform(0, 1)
        if u <= target_func(x, *params) / max_val:
            samples.append(x)
    return np.array(samples)

def plot_results(samples, target_func, domain, params, bins=50):
    x_vals = np.linspace(domain[0], domain[1], 1000)
    f_vals = target_func(x_vals, *params)
    plt.figure(figsize=(8, 6))
    plt.hist(samples, bins=bins, density=True, alpha=0.6, color='g', label='Generated Samples')
    plt.plot(x_vals, f_vals, 'r-', linewidth=2, label='f(x) (Target Distribution)')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Generated Random Numbers vs Target Distribution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

a, b, c = 0, 10, 6
n_samples = 10000
max_val = 2 / (b - a) 
domain = (a, b)
np.random.seed(0)
random_numbers = accept_reject_sampling(triangular_distribution_function, domain, n_samples, max_val, a, b, c)
plot_results(random_numbers, triangular_distribution_function, domain, (a, b, c))