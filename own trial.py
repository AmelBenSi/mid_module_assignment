import sys
NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8, 4, NO_PATH],
    [NO_PATH, 0, 5, NO_PATH, NO_PATH, 3],
    [NO_PATH, NO_PATH, 0, 2, 2, 9],
    [1, NO_PATH, NO_PATH, 0, 3, 7],
    [NO_PATH, 2, NO_PATH, 5, 0, 5],
    [NO_PATH, NO_PATH, NO_PATH, 3, 1, 0]
]


# Python application for Floyd Warshall Algorithm using Recursion

# find number of nodes (n) in an input graph
def floyd(distance):
    n = len(distance)
    print(f"the number of nodes: {n}")
# find the shortest path possible in the graph

    def shortest_path(start_node, end_node, intermediate):
        if intermediate == -1:
            return distance[start_node][end_node]
        else:
            return min(shortest_path(start_node, end_node, intermediate - 1),
                       shortest_path(start_node, intermediate, intermediate-1) +
                       shortest_path(intermediate, end_node, intermediate-1))


# refer to start_node by i
# refer to end_node by j
# refer to intermediate node by k
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
            else:
                distance[i][j] = shortest_path(i, j, n-1)
            j += 1
        i += 1

    print(f"the output graph:\n{distance}")


print(f"the input graph:\n{graph}")
floyd(graph)
