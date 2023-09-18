# Imperative Implementation of the Floyd-Warshall Algorithm

import itertools


def floyd_imp(distance):
    max_length = len(distance)

    for intermediate, start_node, end_node in itertools.product(range(max_length), range(max_length),
                                                                range(max_length)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])

    print(distance)

    return distance