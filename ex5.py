import random
import timeit
import bisect
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Linear search implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary search using bisect
def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1

# Function to measure search time
def measure_search_time(search_func, arr, num_trials=1000, num_iterations=100):
    total_time = 0
    for _ in range(num_trials):
        target = random.choice(arr)  # Pick a random element
        time_taken = timeit.timeit(lambda: search_func(arr, target), number=num_iterations)
        total_time += time_taken
    return total_time / num_trials  # Average time per trial

# List of vector sizes
sizes = [1000, 2000, 4000, 8000, 16000, 32000]

# Store results
lin_times = []
bin_times = []

# Measure performance
for size in sizes:
    sorted_vec = sorted(random.randint(1, 1000000) for _ in range(size))  # Sorted random list
    
    lin_time = measure_search_time(linear_search, sorted_vec)
    bin_time = measure_search_time(binary_search, sorted_vec)
    
    lin_times.append(lin_time)
    bin_times.append(bin_time)
    print(f"Size: {size}, Linear Search: {lin_time:.6f} sec, Binary Search: {bin_time:.6f} sec")

# Define fitting functions
def linear_fit(x, a, b):  # O(n)
    return a * x + b

def log_fit(x, a, b):  # O(log n)
    return a * np.log2(x) + b

# Fit functions with initial guesses
lin_params, _ = curve_fit(linear_fit, sizes, lin_times, p0=[1e-6, 1e-3])
bin_params, _ = curve_fit(log_fit, sizes, bin_times, p0=[1e-6, 1e-3])

# Generate smooth curves for plotting
x_vals = np.linspace(min(sizes), max(sizes), 100)
lin_fit_vals = linear_fit(x_vals, *lin_params)
bin_fit_vals = log_fit(x_vals, *bin_params)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(sizes, lin_times, 'ro', label="Linear Search (Measured)")
plt.plot(x_vals, lin_fit_vals, 'r-', label=f"Linear Fit: {lin_params[0]:.2e} * n + {lin_params[1]:.2e}")

plt.plot(sizes, bin_times, 'bo', label="Binary Search (Measured)")
plt.plot(x_vals, bin_fit_vals, 'b-', label=f"Log Fit: {bin_params[0]:.2e} * log(n) + {bin_params[1]:.2e}")

plt.xlabel("Vector Size")
plt.ylabel("Average Search Time (Seconds)")
plt.title("Linear vs. Binary Search Performance")
plt.legend()
plt.grid()
plt.show()

# Discussion of results
# Comments discussing the results
# For each interpolating function, describe:
# (1) The type of function:
#     - Linear Search Fit: Linear function (O(n))
#     - Binary Search Fit: Logarithmic function (O(log n))

# (2) The parameters of the function:
#     - Linear Search Fit parameters: a={lin_params[0]:.2e}, b={lin_params[1]:.2e}
#         - 'a' represents the slope of the linear function, indicating the rate at
#         - which the search time increases with the size of the vector.
#         - 'b' represents the y-intercept of the linear function, indicating the 
#         - base search time when the vector size is zero.
#     - Binary Search Fit parameters: a={bin_params[0]:.2e}, b={bin_params[1]:.2e}
#         - 'a' represents the coefficient of the logarithmic function, indicating
#         - the rate at which the search time increases with the logarithm of the vector size.
#         - 'b' represents the y-intercept of the logarithmic function, indicating
#         - the base search time when the vector size is one.

# Are the results what you expected? Why?
# - Yes, the results are as expected. Linear search has a linear time complexity (O(n)),
# meaning the search time increases linearly with the size of the vector.
# - Binary search has a logarithmic time complexity (O(log n)), meaning the search time
# increases logarithmically with the size of the vector, making it much more efficient
# for larger datasets.