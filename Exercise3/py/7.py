import numpy as np
import matplotlib.pyplot as plt

NUM_DRONES = 3
AREA_SIZE = 10
BATTERY_RANGE = 15
MAX_PAYLOAD = 5
DRONE_SPEED = 50
NUM_PACKAGES = 50

def generate_packages(num_packages, area_size):
    locations = np.random.uniform(0, area_size, size=(num_packages, 2))
    weights = np.random.uniform(1, MAX_PAYLOAD, num_packages)
    arrival_times = np.cumsum(np.random.exponential(scale=1, size=num_packages))
    return locations, weights, arrival_times

def calculate_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def assign_drone(drone_positions, drone_battery, package_location, package_weight):
    for idx, (position, battery) in enumerate(zip(drone_positions, drone_battery)):
        distance = calculate_distance(position, package_location)
        if battery >= 2 * distance and package_weight <= MAX_PAYLOAD:
            return idx, distance
    return None, None

def simulate_drones(num_drones, packages, battery_range, speed):
    locations, weights, arrival_times = packages
    drone_positions = np.zeros((num_drones, 2))
    drone_battery = np.full(num_drones, battery_range)
    total_distance = 0
    delivery_times = []
    current_time = 0

    for package_idx, package_time in enumerate(arrival_times):
        current_time = package_time
        package_location = locations[package_idx]
        package_weight = weights[package_idx]

        drone_idx, distance = assign_drone(drone_positions, drone_battery, package_location, package_weight)
        if drone_idx is not None:
            travel_time = (2 * distance) / speed
            total_distance += 2 * distance
            delivery_times.append(current_time + travel_time)
            drone_positions[drone_idx] = package_location
            drone_battery[drone_idx] -= 2 * distance

    avg_delivery_time = np.mean(delivery_times)
    return avg_delivery_time, total_distance, locations

def plot_simulation(locations, area_size):
    plt.figure(figsize=(8, 8))
    plt.scatter(locations[:, 0], locations[:, 1], c='blue', label='Packages', alpha=0.7)
    plt.scatter(0, 0, c='red', label='Drone Base', s=100)
    plt.xlim(0, area_size)
    plt.ylim(0, area_size)
    plt.title('Package Delivery Map')
    plt.xlabel('X (km)')
    plt.ylabel('Y (km)')
    plt.legend()
    plt.grid(True)
    plt.show()

packages = generate_packages(NUM_PACKAGES, AREA_SIZE)
avg_delivery_time, total_distance, locations = simulate_drones(NUM_DRONES, packages, BATTERY_RANGE, DRONE_SPEED)
print(f"Average Delivery Time: {avg_delivery_time:.2f} hours")
print(f"Total Distance Traveled by All Drones: {total_distance:.2f} km")
plot_simulation(locations, AREA_SIZE)