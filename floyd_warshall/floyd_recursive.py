# Recursive Implementation of the Floyd-Warshall Algorithm

import itertools


def floyd(distance):

    # Find the number of nodes (max_length) in a graph
    max_length = len(distance)

    # Find the shortest path between all pairs of nodes
    def shortest_path(start_node, end_node, intermediate):

        # If there are no intermediate nodes involved,
        # the shortest path is the direct path between start_node and end_node,
        # This condition represents the last item that stops the recursion loop
        if intermediate < 0:
            return distance[start_node][end_node]

        # Return all possible paths and find the minimum
        else:
            return min(shortest_path(start_node, end_node, intermediate - 1),
                       shortest_path(start_node, intermediate, intermediate - 1) +
                       shortest_path(intermediate, end_node, intermediate - 1))

    # Iterate through each start and end node
    # Assign new names to start_node end_node parameters outside the shortest_path function
    # param i: start_node
    # param j: end_node
    for i, j, in itertools.product(range(max_length), range(max_length)):

        # Initialize the distance of the node to itself as 0
        if i == j:
            distance[i][j] = 0

        else:
            distance[i][j] = shortest_path(i, j, max_length - 1)

        # Check for negative edge weight cycle (currently commented out)
        # if shortest_path(i, i, max_length-1) < 0:
        #    return "negative edge weight cycle!"

    print(distance)

    return distance
