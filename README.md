# Recursive Implementation of Floyd-Warshall 
This is a Python code to solve the Floyd Warshall algorithm using recursion. The Floyd-Warshall algorithm is used for finding the shortest paths between all pairs of vertices in a weighted graph.
## How to install
To install the necessary packages, run the following command:

```bash
pip install -r requirements.txt
```

## How to use
Import the function to your script and insert a graph, as per the following example

```bash
# Import the function
from floyd_warshall.floyd_recursive import floyd

import sys
NO_PATH = sys.maxsize

# Provide an example of a graph
graph = [
    [0, 5, NO_PATH, 10],
    [NO_PATH, 0, 3, NO_PATH],
    [NO_PATH, NO_PATH, 0, 1],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# Call the function using the input graph and print the output
print(floyd(graph))

```
## How to run Unit Tests
Run the following command in the terminal:
```bash
python -m unittest tests\test_unit.py 

```
If you are running the code on the MS DOS command line, use py -m unittest tests\test_unit.py 

## How to run Performance Tests
Run the following command in the terminal:
```bash
python -m cProfile tests/test_performance.py
```
If you are running the code on the MS DOS command line, use py -m cProfile tests/test_performance.py

## How to contribute
Any contributions are welcome! If you want to suggest any changes to optimise the code, please fork the repo and create a pull request.

## Licence
Distributed under the MIT Licence. See License.txt for more information.

