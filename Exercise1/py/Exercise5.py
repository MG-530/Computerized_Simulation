import numpy as np
import matplotlib.pyplot as plt
def generate_points_in_ellipse(a, b, n):
    theta = np.random.uniform(0, 2 * np.pi, n)
    r = np.sqrt(np.random.uniform(0, 1, n))
    x = a * r * np.cos(theta)
    y = b * r * np.sin(theta)
    return x, y
def plot_ellipse(a, b):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    plt.plot(x, y, color='blue', linewidth=2, label='Ellipse boundary')
a, b = 5, 3
n_values = [100, 1000, 10000]
for n in n_values:
    x, y = generate_points_in_ellipse(a, b, n)
    plt.figure()
    plot_ellipse(a, b)  
    plt.scatter(x, y, s=1, color='red', label='Random points')  
    plt.title(f'Uniform Points in Ellipse for n={n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.legend()
    plt.show()
