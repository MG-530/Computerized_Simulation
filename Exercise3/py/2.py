import numpy as np
import matplotlib.pyplot as plt

def scattering_distribution(x):
    return np.cos(x)**2

def accept_reject_sampling(target_func, domain, n_samples, max_val):
    samples = []
    x_min, x_max = domain
    while len(samples) < n_samples:
        x = np.random.uniform(x_min, x_max)
        u = np.random.uniform(0, 1)
        if u <= target_func(x) / max_val:
            samples.append(x)
    return np.array(samples)

def plot_results(samples, target_func, domain, bins=50):
    x_vals = np.linspace(domain[0], domain[1], 1000)
    f_vals = target_func(x_vals)
    plt.figure(figsize=(8, 6))
    plt.hist(samples, bins=bins, density=True, alpha=0.6, color='g', label='Generated Samples')
    plt.plot(x_vals, f_vals / np.max(f_vals), 'r-', linewidth=2, label='Normalized f(x)')
    plt.xlabel('x (radians)')
    plt.ylabel('Probability Density')
    plt.title('Generated Scattering Angles vs True Distribution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

n_samples = 10000
domain = (0, np.pi)
max_val = 1
np.random.seed(0)
scattering_angles = accept_reject_sampling(scattering_distribution, domain, n_samples, max_val)
plot_results(scattering_angles, scattering_distribution, domain)