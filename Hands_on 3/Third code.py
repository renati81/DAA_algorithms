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
n_values = np.arange(1, 1000, 10)  # Example: testing n values from 1 to 1000 in steps of 10
times = []

for n in n_values:
    start_time = time.time()  # Start time
    f(n)  # Call the function
    end_time = time.time()  # End time
    times.append(end_time - start_time)  # Store the elapsed time

# Fit a quadratic polynomial to the timing data
coeffs = np.polyfit(n_values, times, 2)  # Polynomial fit of degree 2 (quadratic)
poly_fit = np.poly1d(coeffs)  # Create polynomial function from the coefficients

# Create upper and lower bounds
upper_bound = 1.5 * (n_values ** 2)  # Upper bound: 1.5 * n^2
lower_bound = 0.5 * (n_values ** 2)  # Lower bound: 0.5 * n^2

# Plotting the actual times
plt.plot(n_values, times, label="Actual Time", color="blue")

# Plotting the polynomial fit
plt.plot(n_values, poly_fit(n_values), label="Quadratic Fit", linestyle="--", color="green")

# Plotting the upper bound
plt.plot(n_values, upper_bound, label="Upper Bound (O(n^2))", linestyle=":", color="red")

# Plotting the lower bound
plt.plot(n_values, lower_bound, label="Lower Bound (Ω(n^2))", linestyle="-.", color="orange")

# Adding labels and legend
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Time vs n with Upper and Lower Bounds")
plt.legend()

# Show the plot
plt.show()
