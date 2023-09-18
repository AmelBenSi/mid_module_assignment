# Performance tests for the floyd function

""" The file tests the performance of the code using 3 Graph sizes:

Small graph of Test Case 1, medium-size graph of Test Case 9 and very large graph of Test Case 8.

The code section that detects the existence of a negative edge weight cycle was commented out,
when running the performance tests below.
To analyse the impact of adding the block of code that detects an edge weight cycle,
we compared performance before and after adding this block of code using Test Case 1.
The number of function calls and execution time were noted. More details are in the report.

Then, the performance of the recursive version of the algorithm is tested against the imperative version,
using the very large graph of Test Case 8.
"""

# Import the functions
from floyd_warshall.floyd_recursive import floyd
from floyd_warshall.floyd_imperative import floyd_imp


# Import test cases
from tests.test_cases import input_performance, input_reference, input_veryLarge


# Import the cProfile module
import cProfile

# Test performance using a small graph of 4 nodes
print("Performance of the recursive version of the algorithm using a 4-nodes graph:")
cProfile.run("floyd(input_reference)")

# Test performance using a medium-size graph of 10 nodes
print("Performance of the recursive version of the algorithm using 10-nodes graph:")
cProfile.run("floyd(input_performance)")

# Test performance using a large graph of 16 nodes
# The code below is commented out because the execution time can be very long
# Uncomment to run it
# print("Performance of the recursive version of the algorithm using 16 nodes graph ")
# cProfile.run("floyd(input_veryLarge)")

# Compare performance between the imperative and recursive versions of the Floyd Warshall Algorithm
print("Performance of the imperative version of the algorithm using 16-nodes graph: ")
cProfile.run("floyd_imp(input_veryLarge)")
