import random
import time

class Vehicle:
    def __init__(self, vehicle_type, position):
        self.type = vehicle_type
        self.position = position
        self.speed = random.randint(1, 3) 
class TrafficLight:
    def __init__(self):
        self.state = "green"
        self.timer = 0
        self.cycle_duration = random.randint(10, 30)
    def update(self):
        self.timer += 1
        if self.timer >= self.cycle_duration:
            self.timer = 0
            self.state = "red" if self.state == "green" else "green"
        return self.state
class Road:
    def __init__(self,traffic):
        self.vehicles = []
        self.traffic_light = TrafficLight()
        self.max_vehicles = 10
        self.traffic= traffic

    def generate_vehicle(self):
        if len(self.vehicles) < self.max_vehicles:
            vehicle_types = ["car", "truck"]
            new_vehicle = Vehicle(
                random.choice(vehicle_types),0)
            self.vehicles.append(new_vehicle)

    def move_vehicles(self):
        light_state = self.traffic_light.update()
        for vehicle in self.vehicles[:]:
            # Stop at red light
            if light_state == "red" :
                continue
            vehicle.position += vehicle.speed
            if vehicle.position > 20:
                self.vehicles.remove(vehicle)

    def simulate(self, iterations=50):
        print(f"Traffic Flow Simulation Time for traffic light:{self.traffic_light.cycle_duration }")
        print("-" * 30)
        for _ in range(iterations):
            if random.random() < self.traffic:  
                self.generate_vehicle()
            self.move_vehicles()
            self.print_road_state()
            time.sleep(0.5) 
    def print_road_state(self):
        road = ["-"] * 20
        light_symbol = "🟢" if self.traffic_light.state == "green" else "🔴"
        for vehicle in self.vehicles:
            if 0 <= vehicle.position < 20:
                road[int(vehicle.position)] = "🚘" if vehicle.type == "car" else "⛟"
        print(f"Traffic Light: {light_symbol}{self.traffic_light.cycle_duration - self.traffic_light.timer}")
        print("Road: " + "".join(road))
        print(f"Vehicles: {len(self.vehicles)}")
        print("-" * 30)
        print()


def main():
    #random.seed(42) 
    road = Road(0.3)
    road.simulate()

if __name__ == "__main__":
    main()