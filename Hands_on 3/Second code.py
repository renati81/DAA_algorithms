import time
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(n)
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1

# Timing the function for different values of n
n_values = range(1, 1000, 10)
times = []

for n in n_values:
    start_time = time.time()  # Start time
    f(n)  # Call the function
    end_time = time.time()  # End time
    times.append(end_time - start_time)

# Plotting time vs n
plt.plot(n_values, times, label="Time taken")

# Polynomial fit to the data (degree 2 polynomial since we expect O(n^2))
coeffs = np.polyfit(n_values, times, 2)  
poly_fit = np.poly1d(coeffs)

# Plotting the polynomial fit
plt.plot(n_values, poly_fit(n_values), label="Polynomial fit", linestyle="-")

plt.xlabel("n")
plt.ylabel("Time (s)")
plt.legend()
plt.show()
