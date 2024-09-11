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

# Timing the function
for n in n_values:
    start_time = time.time()  # Start time
    f(n)  # Call the function
    end_time = time.time()  # End time
    elapsed_time = end_time - start_time
    times.append(elapsed_time if elapsed_time > 0 else 0)  # Store only positive time

# Fit a quadratic polynomial to the timing data
coeffs = np.polyfit(n_values, times, 2)  # Polynomial fit of degree 2 (quadratic)
poly_fit = np.poly1d(coeffs)  # Create polynomial function from the coefficients

# Plotting the actual times and the fitted polynomial
plt.figure(figsize=(12, 6))

# Full graph with actual times and polynomial fit
plt.subplot(1, 2, 1)
plt.plot(n_values, times, label="Actual Time", color="blue")
plt.plot(n_values, poly_fit(n_values), label="Quadratic Fit", linestyle="--", color="green")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Time vs n (Full Range)")
plt.legend()

# Zoomed-in graph to find n_0
plt.subplot(1, 2, 2)
plt.plot(n_values, times, label="Actual Time", color="blue")
plt.plot(n_values, poly_fit(n_values), label="Quadratic Fit", linestyle="--", color="green")

# Indicate an approximate value for n_0
n_0 = 150  # Adjust based on visual inspection
plt.axvline(x=n_0, color='red', linestyle='--', label=f"Approximate n_0 = {n_0}")

# Zoom in to focus on n_0
plt.xlim(0, 300)  # Zoom range for n
plt.ylim(0, max(times[:30]))  # Focus on the y-limit to highlight n_0 region

# Highlight the zoomed-in area
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Zoomed-in View to Find n_0")
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
