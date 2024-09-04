#CPU: Intel Core i5s
#RAM: 12.0 GB (11.7 GB usable)
#Storage: 512 GB SSD
#Operating System: Windows 11
import time
import random
import matplotlib.pyplot as plt

#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#benchmarking algorithm
def benchmark_sorting_algorithm(sorting_func, input_sizes):
    times = []
    for size in input_sizes:
        arr = random.sample(range(size * 10), size)
        start_time = time.time()
        sorting_func(arr.copy())
        end_time = time.time()
        times.append(end_time - start_time)
    return times

#input sizes
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

#benchmarking each algorithms
insertion_times = benchmark_sorting_algorithm(insertion_sort, input_sizes)
selection_times = benchmark_sorting_algorithm(selection_sort, input_sizes)
bubble_times = benchmark_sorting_algorithm(bubble_sort, input_sizes)

#plotting the sizes
plt.plot(input_sizes, insertion_times, label="Insertion Sort", marker='o')
plt.plot(input_sizes, selection_times, label="Selection Sort", marker='o')
plt.plot(input_sizes, bubble_times, label="Bubble Sort", marker='o')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Benchmark of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
