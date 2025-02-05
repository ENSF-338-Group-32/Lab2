#3.3.1 A profile is a set of statistics that describes 
#      how often and for how long various parts of the program 
#      executed. A profiler is simply a preexisting function 
#      that can be used to collect that information

#3.3.2 Benchmarking is used to measure the time of a whole 
#      operation so you can compare software on different 
#      hardwares or different versions of the same software
#      and typically is just a single number of total runtime 
#      whereas profiling is used to break down the behaviour 
#      of the program and identify any sort of bottlenecking 
#      that may be occuring at some point, limiting the codes 
#      efficiency

#3.3.3 

import timeit
import cProfile

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n *sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
#third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


profiler = cProfile.Profile()
profiler.enable()
    
test_function()
third_function()
    
profiler.disable()
profiler.print_stats(sort="time")

#3.3.4  
#  68 function calls (23 primitive calls) in 10.060 seconds

#  Ordered by: internal time

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1   10.057   10.057   10.057   10.057 ex3.py:35(third_function)
#       1    0.003    0.003    0.003    0.003 {method 'disable' of '_lsprof.Profiler' objects}
#   55/10    0.000    0.000    0.000    0.000 ex3.py:22(sub_function)
#       1    0.000    0.000    0.000    0.000 ex3.py:29(test_function)
#      10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#      ncalls is number of times a function was called
#      tottime is total time spent within the function excluding calls to other function
#      percall is time spent per function call
#      cumtime is the total time spent in the function including calls to sub functions
#      filename:lineno(function) shows the file name, line number, and function name

#      The majority of the runtime is dominated by third_function 
#      as it iterates through 100 million numbers, computing squares 
#      whereas test_function only iterates 10 times and calls 
#      sub_function which calculates small factorials using recursion 
#      but only up to 9!



