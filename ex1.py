def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)

#1.1 This is a basic function that computes the fibonacci
#    sequence up to a given integer n

#1.2 The code provided is not a divide and conquer algorithm
#    as there is no use of independent subproblems as the 
#    code simply recomputes overlapping subproblems, there 
#    is also no explicit merge step where the data is reconciled 
#    efficiently, instead it simply adds the two values

#1.3  This recursive implementation has a time complexity of 
#     O(2^n) as each call to the function makes two recursive 
#     calls, forming a binary recursion tree with a height of 
#     O(n) where the total calls grow exponentially

#1.4

def func2(n, memo={}):  # Default argument acts as a cache
    if n == 0 or n == 1:
        return n
    if n in memo:  # Check if result is already computed
        return memo[n]
    
    memo[n] = func2(n-1, memo) + func2(n-2, memo)  # Store result
    return memo[n]


#1.5 The new optimized algorithm has reduced the time complexity 
#    from O(2^n) down to just simply O(n) as now the results are 
#    cached and only need to be calculated 


# 1.6
import time
import matplotlib.pyplot as plt

original_times = []
for i in range(36):
    start_time = time.time()
    func1(i)
    end_time = time.time()
    original_times.append(end_time - start_time)

optimized_times = []
for i in range(36):
    start_time = time.time()
    func2(i)
    end_time = time.time()
    optimized_times.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(36), original_times, label='Original Function', color='blue')
plt.plot(range(36), optimized_times, label='Optimized Function (Memoization)', color='red')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Fibonacci Functions')
plt.legend()
plt.grid(True)
plt.savefig('ex1.6.1.jpg')

# Display the plot
plt.show()

# Saving the optimized version's times for a second plot
plt.figure(figsize=(10, 6))
plt.plot(range(36), optimized_times, label='Optimized Function (Memoization)', color='red')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Optimized Fibonacci Function')
plt.legend()
plt.grid(True)
plt.savefig('ex1.6.2.jpg')