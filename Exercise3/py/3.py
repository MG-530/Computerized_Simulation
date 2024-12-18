import numpy as np
import matplotlib.pyplot as plt

def service_time_distribution(x):
    return x * np.exp(-x) if x > 0 else 0

def exponential_distribution(x):
    return np.exp(-x) if x > 0 else 0

def accept_reject_sampling(target_func, proposal_func, domain, n_samples, max_val):
    samples = []
    while len(samples) < n_samples:
        x = np.random.exponential(1) 
        u = np.random.uniform(0, 1)
        if u <= target_func(x) / (max_val * proposal_func(x)):
            samples.append(x)
    return np.array(samples)

def plot_results(samples, target_func, bins=50):
    x_vals = np.linspace(0, max(samples), 1000)
    f_vals = np.array([target_func(x) for x in x_vals])
    plt.figure(figsize=(8, 6))
    plt.hist(samples, bins=bins, density=True, alpha=0.6, color='g', label='Generated Samples')
    plt.plot(x_vals, f_vals / f_vals.max(), 'r-', linewidth=2, label='Normalized f(x)')
    plt.xlabel('x (Service Time)')
    plt.ylabel('Probability Density')
    plt.title(f'Service Times vs True Distribution \n mean:{np.mean(samples)} max:{np.max(samples)} min:{np.min(samples)}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

n_samples = 10000
domain = (0, np.inf)
max_val = 1 / np.exp(1)
np.random.seed(0)
service_times = accept_reject_sampling(service_time_distribution, exponential_distribution, domain, n_samples, max_val)
plot_results(service_times, service_time_distribution)