# Unit tests for the floyd function

# Import floyd function
from recursive.floyd_recursive import floyd

# Import test cases to be tested
from tests.test_cases import (input_reference, input_NegativeEdges, input_NegativeCycle, input_NonIntegerError,
                              input_OneNode, input_twoNodes, input_isolateNode, input_veryLarge, output_reference,
                              output_NegativeEdges, output_NegativeCycle, output_OneNode, output_twoNodes,
                              output_isolateNode, output_veryLarge)

# Import the unittest module
import unittest


# Unit tests
class TestFloyd(unittest.TestCase):

    # Test output compared against the output of the graph provided in the reference
    def test_floyd_reference(self):
        print("\nThe Output of Test Case 1 - Reference graph:")
        self.assertEqual(output_reference, floyd(input_reference), "Incorrect Result!")

    # Test a graph that contains negative edges but no negative cycle
    def test_floyd_negative_edges(self):
        print("\nThe Output of Test Case 2 - Graph with negative edges:")
        self.assertEqual(output_NegativeEdges, floyd(input_NegativeEdges), "Incorrect Result!")

    # Test if the graph contains a negative edge weight cycle
    # Uncomment the related block of code  in the floyd_recursive.py file to run this test
    def test_floyd_negative_cycle(self):
        self.assertEqual(output_NegativeCycle, floyd(input_NegativeCycle), "The graph of Test Case 3 "
                                                                           "does not have a negative weight cycle")

        if True:
            print("Test Case 3 has a negative edge weight cycle!")

    # Test a graph that contains an invalid input
    def test_InputError(self):
        self.assertRaises(TypeError, lambda: floyd(input_NonIntegerError))
        if True:
            print("The Graph of Test Case 4 contains a non-integer value")

    # Test one-node graph
    def test_OneNode(self):
        print("\nThe Output of Test Case 5 - One node graph:")
        self.assertEqual(output_OneNode, floyd(input_OneNode), "Incorrect Result")

    # Test two-nodes graph
    def test_twoNodes(self):
        print("\nThe Output of Test Case 6 - Two nodes graph:")
        self.assertEqual(output_twoNodes, floyd(input_twoNodes), "Incorrect Result")

    # Test a graph where nodes have no outgoing edges
    def test_isolateNode(self):
        print("\nThe Output of Test Case 7 - Isolated nodes graph:")
        self.assertEqual(output_isolateNode, floyd(input_isolateNode), "Incorrect Result")

    # Test a large graph that contains 16 nodes
    # Uncomment before running this test
    # def test_floyd_large(self):
    #    print("\nThe Output of Test Case 8 - Very large graph:")
    #    self.assertEqual(output_veryLarge, floyd(input_veryLarge), "Incorrect Result")


# Run the test
if __name__ == '__main__':
    unittest.main()
