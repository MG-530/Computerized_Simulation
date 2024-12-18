import random
import time

class Vehicle:
    def __init__(self, vehicle_type, position):
        self.type = vehicle_type
        self.position = position
        self.speed = random.randint(1, 3)
        self.wait_time = 0
        self.safe_distance = 2 

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
    def __init__(self, traffic):
        self.vehicles = []
        self.traffic_light = TrafficLight()
        self.max_vehicles = 10
        self.traffic = traffic
        self.stats = {
            "total_vehicles": 0,
            "passed_vehicles": 0,
            "total_wait_time": 0
        }
        self.intersection_pos = 10

    def check_collision(self, position):
        for vehicle in self.vehicles:
            if abs(vehicle.position - position) < vehicle.safe_distance:
                return True
        return False

    def generate_vehicle(self):
        if len(self.vehicles) < self.max_vehicles:
            if not self.check_collision(0):
                vehicle_types = ["car", "truck"]
                new_vehicle = Vehicle(random.choice(vehicle_types), 0)
                self.vehicles.append(new_vehicle)
                self.stats["total_vehicles"] += 1

    def can_move_forward(self, vehicle):
        next_position = vehicle.position + vehicle.speed
        
        if self.traffic_light.state == "red" and \
           self.intersection_pos - 1 <= next_position <= self.intersection_pos:
            return False
            
        for other_vehicle in self.vehicles:
            if other_vehicle != vehicle and \
               other_vehicle.position > vehicle.position and \
               abs(other_vehicle.position - next_position) < vehicle.safe_distance:
                return False
        return True

    def move_vehicles(self):
        light_state = self.traffic_light.update()
        for vehicle in self.vehicles[:]:
            if light_state == "red" and self.intersection_pos - 1 <= vehicle.position <= self.intersection_pos:
                vehicle.wait_time += 1
                self.stats["total_wait_time"] += 1
                continue
                
            if self.can_move_forward(vehicle):
                vehicle.position += vehicle.speed
            else:
                vehicle.wait_time += 1
                self.stats["total_wait_time"] += 1
                
            if vehicle.position > 20:
                self.vehicles.remove(vehicle)
                self.stats["passed_vehicles"] += 1

    def simulate(self, iterations=50):
        print(f"Traffic Flow Simulation Time for traffic light: {self.traffic_light.cycle_duration}")
        print("-" * 30)
        for _ in range(iterations):
            if random.random() < self.traffic:
                self.generate_vehicle()
            self.move_vehicles()
            self.print_road_state()
            time.sleep(0.5)
        self.print_final_stats()

    def print_road_state(self):
        road = ["-"] * 10 + ["|" if self.traffic_light.state == "red" else "-"] + ["-"] * 11
        light_symbol = "🟢" if self.traffic_light.state == "green" else "🔴"
        for vehicle in self.vehicles:
            if 0 <= vehicle.position < 20:
                road[int(vehicle.position)] = "🚘" if vehicle.type == "car" else "🚚"
        print(f"Traffic Light: {light_symbol}{self.traffic_light.cycle_duration - self.traffic_light.timer}")
        print("Road: " + "".join(road))
        print(f"Vehicles on road: {len(self.vehicles)}")
        print(f"Vehicles passed: {self.stats['passed_vehicles']}")
        if self.stats['total_vehicles'] > 0:
            avg_wait = self.stats['total_wait_time'] / self.stats['total_vehicles']
            print(f"Average wait time: {avg_wait:.2f}")
        print("-" * 30)
        print()

    def print_final_stats(self):
        print("\nFinal Statistics:")
        print(f"Total vehicles generated: {self.stats['total_vehicles']}")
        print(f"Total vehicles passed: {self.stats['passed_vehicles']}")
        if self.stats['total_vehicles'] > 0:
            avg_wait = self.stats['total_wait_time'] / self.stats['total_vehicles']
            print(f"Average wait time per vehicle: {avg_wait:.2f}")
            throughput = self.stats['passed_vehicles'] / self.stats['total_vehicles'] * 100
            print(f"Traffic throughput: {throughput:.1f}%")

def main():
    road = Road(0.3)
    road.simulate()

if __name__ == "__main__":
    main()