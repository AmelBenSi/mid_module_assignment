# Test Cases for floyd function

""" This is a summary of the coverage of the unit tests

The Floyd Warshall algorithm function is tested in eight test cases, presented below.
It can handle all types of graphs from small to large and with negative edges.
It also detects negative weight cycles.
"""

import sys

# maxsize (infinity) if there is no edge between two nodes
NO_PATH = sys.maxsize

# Test Case 1: Graph of 4 nodes
# from the reference provided by the University of Liverpool
""" 
Title: Floyd Warshall Algorithm | DP-16
Author: GeeksforGeeks
Date: 07 Jul, 2023
Available at: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""
input_reference = [
    [0, 5, NO_PATH, 10],
    [NO_PATH, 0, 3, NO_PATH],
    [NO_PATH, NO_PATH, 0, 1],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

output_reference = [
    [0, 5, 8, 9],
    [NO_PATH, 0, 3, 4],
    [NO_PATH, NO_PATH, 0, 1],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]


# Test Case 2: Graph containing negative edges but no negative cycles
input_NegativeEdges = [
    [0, 5, NO_PATH, 12, NO_PATH],
    [6, 0, 3, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 0, 6, NO_PATH],
    [8, 2, NO_PATH, 0, -6],
    [-3, NO_PATH, 21, NO_PATH, 0]
]

output_NegativeEdges = [
    [0, 5, 8, 12, 6],
    [0, 0, 3, 9, 3],
    [-3, 2, 0, 6, 0],
    [-9, -4, -1, 0, -6],
    [-3, 2, 5, 9, 0]
]


# Test Case 3: Graph that contains a negative cycle
""" 
Title: Detecting negative cycle using Floyd Warshall
Author: GeeksforGeeks
Date: 23 Jun, 2023
Available at: https://www.geeksforgeeks.org/detecting-negative-cycle-using-floyd-warshall/
"""
input_NegativeCycle = [
    [0, 1, NO_PATH, NO_PATH],
    [NO_PATH, 0, -1, NO_PATH],
    [NO_PATH, NO_PATH, 0, -1],
    [-1, NO_PATH, NO_PATH, 0]
]

output_NegativeCycle = "negative edge weight cycle!"


# Test Case 4: Graph that contains an invalid input
input_NonIntegerError = [
    [0, NO_PATH, NO_PATH, 3],
    [NO_PATH, 0, 6, NO_PATH],
    [5, NO_PATH, 0, "string"],
    [NO_PATH, 4, NO_PATH, 0]
]


# Test Case 5: One node graph
input_OneNode = [[3]]
output_OneNode = [[0]]


# Test Case 6: Two-nodes graph
input_twoNodes = [
    [0, 4],
    [NO_PATH, 0]
]

output_twoNodes = [
    [0, 4],
    [NO_PATH, 0]
]


# Test Case 7: Isolated nodes (nodes not connected to other nodes through edges)
input_isolateNode = [
    [0, NO_PATH, NO_PATH],
    [NO_PATH, 0, NO_PATH],
    [NO_PATH, NO_PATH, 0]
]

output_isolateNode = [
    [0, NO_PATH, NO_PATH],
    [NO_PATH, 0, NO_PATH],
    [NO_PATH, NO_PATH, 0]
]


# Test Case 8: Very large Graph of 16 nodes
input_veryLarge = [
    [0, 6, 7, 8, 9, 2, NO_PATH, 6, 8, 4, NO_PATH, 4, 6, 5, 6, NO_PATH],
    [6, 0, NO_PATH, 4, 3, 2, 8, 2, 2, 3, NO_PATH, 9, 1, 6, 5, 5],
    [2, 3, 0, 11, 5, NO_PATH, 8, 3, 8, NO_PATH, 12, NO_PATH, 9, NO_PATH, 2, 6],
    [NO_PATH, 2, 5, 0, 6, 8, 6, NO_PATH, 9, 1, 1, 3, NO_PATH, 4, 9, 8],
    [9, 6, NO_PATH, 2, 0, 7, 3, 9, 2, 5, 7, 2, 5, 2, 33, 9],
    [6, 2, 2, 8, 4, 0, 5, NO_PATH, 8, 2, 6, 2, 7, 6, 8, 22],
    [4, 4, NO_PATH, 2, 8, 5, 0, 4, 2, NO_PATH, 22, 4, 8, 2, 1, NO_PATH],
    [6, 4, NO_PATH, 5, 3, 5, NO_PATH, 0, 8, 3, 2, 3, 6, 3, 1, 8],
    [3, 2, 6, 5, 3, 6, 8, 3, 0, 7, NO_PATH, 5, 4, 5, 6, 6],
    [NO_PATH, 4, NO_PATH, 4, NO_PATH, 4, 5, 9, 3, 0, 4, 8, 3, NO_PATH, 4, 9],
    [6, 7, 4, 3, NO_PATH, 7, NO_PATH, 8, 2, 9, 0, NO_PATH, 4, 8, 8, 9],
    [4, 6, 4, 8, 2, 8, NO_PATH, 3, 9, 4, 3, 0, NO_PATH, 5, NO_PATH, 9],
    [NO_PATH, 3, 2, 9, 6, 3, NO_PATH, 4, 6, 4, NO_PATH, 2, 0, 5, 2, NO_PATH],
    [4, 3, NO_PATH, 9, 4, 3, 2, 8, 4, 2, 8, 5, 3, 0, 3, 5],
    [7, 3, 9, 4, 3, 1, 2, 5, NO_PATH, 3, 7, NO_PATH, 3, 2, 0, 4],
    [4, NO_PATH, 6, 7, 8, NO_PATH, 8, 5, 4, 2, 9, 4, 3, NO_PATH, 3, 0],
]

output_veryLarge = [
    [0, 4, 4, 8, 6, 2, 7, 6, 6, 4, 7, 4, 5, 5, 6, 9],
    [5, 0, 3, 4, 3, 2, 5, 2, 2, 3, 4, 3, 1, 5, 3, 5],
    [2, 3, 0, 6, 5, 3, 4, 3, 5, 5, 5, 5, 4, 4, 2, 6],
    [6, 2, 5, 0, 5, 4, 6, 4, 3, 1, 1, 3, 3, 4, 5, 7],
    [5, 4, 6, 2, 0, 5, 3, 5, 2, 3, 3, 2, 5, 2, 4, 7],
    [4, 2, 2, 6, 4, 0, 5, 4, 4, 2, 5, 2, 3, 6, 4, 7],
    [4, 4, 4, 2, 4, 2, 0, 4, 2, 3, 3, 4, 4, 2, 1, 5],
    [6, 4, 4, 5, 3, 2, 3, 0, 4, 3, 2, 3, 4, 3, 1, 5],
    [3, 2, 5, 5, 3, 4, 6, 3, 0, 5, 5, 5, 3, 5, 4, 6],
    [6, 4, 5, 4, 6, 4, 5, 6, 3, 0, 4, 5, 3, 6, 4, 8],
    [5, 4, 4, 3, 5, 6, 8, 5, 2, 4, 0, 6, 4, 7, 6, 8],
    [4, 6, 4, 4, 2, 5, 5, 3, 4, 4, 3, 0, 7, 4, 4, 8],
    [4, 3, 2, 6, 4, 3, 4, 4, 5, 4, 5, 2, 0, 4, 2, 6],
    [4, 3, 5, 4, 4, 3, 2, 5, 4, 2, 5, 5, 3, 0, 3, 5],
    [5, 3, 3, 4, 3, 1, 2, 5, 4, 3, 5, 3, 3, 2, 0, 4],
    [4, 6, 5, 6, 6, 4, 5, 5, 4, 2, 6, 4, 3, 5, 3, 0]
]

# Test Case 9: Medium-size graph of 10 nodes
# This graph will only be used to test performance
input_performance = [
    [0, 4, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 7, 4, NO_PATH, NO_PATH],
    [NO_PATH, 0, 9, NO_PATH, NO_PATH, 6, 8, 1, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 0, NO_PATH, 10, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 10, NO_PATH],
    [NO_PATH, NO_PATH, 8, 6, 0, 5, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 6, 0, NO_PATH, NO_PATH, 8, 5],
    [NO_PATH, 4, NO_PATH, NO_PATH, NO_PATH, 7, 0, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 8],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 6, 0]
]
