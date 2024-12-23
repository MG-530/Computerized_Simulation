import numpy as np
import matplotlib.pyplot as plt

def rayleigh_samples(n, sigma):
    U = np.random.uniform(0, 1, n)
    return sigma * np.sqrt(-2 * np.log(U))

def rayleigh_pdf(x, sigma):
    return (x / sigma**2) * np.exp(-x**2 / (2 * sigma**2))

def plot_results(samples, pdf_func, sigma, bins=50):
    x_vals = np.linspace(0, max(samples), 1000)
    f_vals = pdf_func(x_vals, sigma)
    plt.figure(figsize=(8, 6))
    plt.hist(samples, bins=bins, density=True, alpha=0.6, color='g', label='Generated Samples')
    plt.plot(x_vals, f_vals, 'r-', linewidth=2, label='f(x) (Rayleigh PDF)')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Rayleigh Distribution (σ={})'.format(sigma))
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

n_samples = 10000
sigma = 2
samples = rayleigh_samples(n_samples, sigma)
plot_results(samples, rayleigh_pdf, sigma)
