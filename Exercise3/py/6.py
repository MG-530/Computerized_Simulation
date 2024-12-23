import numpy as np

def sample_exponential(rate):
    return np.random.exponential(1 / rate)

def simulate_bank(num_counters, arrival_rate, service_rate, simulation_time):
    current_time = 0
    next_arrival = sample_exponential(arrival_rate)
    counters_free_at = [0] * num_counters  
    waiting_queue = []  
    total_waiting_times = []  
    total_system_times = [] 
    counter_usage = [0] * num_counters  

    while current_time <= simulation_time:
        next_departure = min([t for t in counters_free_at if t > current_time], default=float('inf'))

        if next_arrival < next_departure:
            current_time = next_arrival
            # Check for free counters
            free_counters = [i for i, t in enumerate(counters_free_at) if t <= current_time]
            if free_counters:
                # Assign to a free counter
                assigned_counter = free_counters[0]
                service_time = sample_exponential(service_rate)
                counters_free_at[assigned_counter] = current_time + service_time
                counter_usage[assigned_counter] += service_time
                total_system_times.append(service_time) 
            else:
                waiting_queue.append(current_time)
            next_arrival = current_time + sample_exponential(arrival_rate)
        elif next_departure != float('inf'):
            current_time = next_departure
            finished_counter = counters_free_at.index(next_departure)
            if waiting_queue:
                waiting_time_start = waiting_queue.pop(0)
                waiting_time = current_time - waiting_time_start
                total_waiting_times.append(waiting_time)
                service_time = sample_exponential(service_rate)
                counters_free_at[finished_counter] = current_time + service_time
                counter_usage[finished_counter] += service_time
                total_system_times.append(waiting_time + service_time)
            else:
                counters_free_at[finished_counter] = 0  # Mark counter as free
        else:
            break  # End simulation if no future events are scheduled

    avg_waiting_time = np.mean(total_waiting_times) if total_waiting_times else 0
    avg_total_system_time = np.mean(total_system_times) if total_system_times else 0
    usage_percentages = [(time / simulation_time) * 100 for time in counter_usage]
    return avg_waiting_time, avg_total_system_time, usage_percentages

num_counters = 3
arrival_rate = 2
service_rate = 3
simulation_time = 5000
avg_waiting, avg_system_time, usage = simulate_bank(num_counters, arrival_rate, service_rate, simulation_time)
print(f"Average Waiting Time: {avg_waiting:.2f}")
print(f"Counter Usage (%): {usage}")
print(f"Average Time in System: {avg_system_time:.2f}")