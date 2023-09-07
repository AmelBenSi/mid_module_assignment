import sys
import itertools

NO_PATH = sys.maxsize

graph = []


# Recursive Implementation of Floyd-Warshall´s Algorithm

def floyd(distance):

    # Find the number of nodes (n) in a graph
    n = len(distance)

    # Find the shortest path between all pairs of nodes
    def shortest_path(start_node, end_node, intermediate):
        # Initialize the distance of the node to itself as 0
        if start_node == end_node:
            return 0

        # Assume that if the shortest path between two nodes does not visit any intermediate node
        # then the shortest path is the direct distance between the start node and end node
        elif intermediate == -1:
            return distance[start_node][end_node]

        # Return all possible paths and find the minimum
        else:
            return min(shortest_path(start_node, end_node, intermediate - 1),
                       shortest_path(start_node, intermediate, intermediate - 1) +
                       shortest_path(intermediate, end_node, intermediate - 1))

    # Iterate through each start and end node
    for start_node, end_node in itertools.product(range(n), range(n)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
        else:
            distance[start_node][end_node] = shortest_path(start_node, end_node, n - 1)
        end_node += 1
        start_node += 1

    print(f"\nThe output graph:\n{distance}")


print(f"\nThe input graph:\n{graph}")
floyd(graph)
