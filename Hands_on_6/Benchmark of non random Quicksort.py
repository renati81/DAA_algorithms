import time
import matplotlib.pyplot as plt
import numpy as np

# Non-Random pivot quicksort (pivot is the last element)
def quicksort_non_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quicksort_non_random(left) + [pivot] + quicksort_non_random(right)

# Helper function to generate input arrays for different cases
def generate_best_case(n):
    # Already sorted array is the best case
    return list(range(n))

def generate_worst_case(n):
    # Reverse sorted array is the worst case
    return list(range(n, 0, -1))

def generate_average_case(n):
    # Random array is the average case
    return np.random.randint(0, 10000, size=n).tolist()

# Benchmarking function for different input sizes
def benchmark_quicksort():
    # Array sizes starting from 10
    sizes = [10, 50, 100, 500, 1000]
    best_times = []
    worst_times = []
    average_times = []
    
    print(f"{'Size (n)':<10} {'Best Case (s)':<20} {'Worst Case (s)':<20} {'Average Case (s)':<20}")
    print("=" * 70)
    
    for n in sizes:
        # Best Case
        best_case = generate_best_case(n)
        start_time = time.time()
        quicksort_non_random(best_case)
        best_time = time.time() - start_time
        best_times.append(best_time)
        
        # Worst Case
        worst_case = generate_worst_case(n)
        start_time = time.time()
        quicksort_non_random(worst_case)
        worst_time = time.time() - start_time
        worst_times.append(worst_time)
        
        # Average Case
        average_case = generate_average_case(n)
        start_time = time.time()
        quicksort_non_random(average_case)
        average_time = time.time() - start_time
        average_times.append(average_time)
        
        # Output the results in table format
        print(f"{n:<10} {best_time:<20.6f} {worst_time:<20.6f} {average_time:<20.6f}")
    
    return sizes, best_times, worst_times, average_times

# Plotting function
def plot_benchmark_results():
    sizes, best_times, worst_times, average_times = benchmark_quicksort()
    
    plt.plot(sizes, best_times, label='Best Case', marker='o')
    plt.plot(sizes, worst_times, label='Worst Case', marker='o')
    plt.plot(sizes, average_times, label='Average Case', marker='o')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Non-Random Pivot Benchmark')
    plt.legend()
    plt.grid(True)
    plt.show()

# Running the benchmark and plot
plot_benchmark_results()
