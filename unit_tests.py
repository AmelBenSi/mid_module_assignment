# Unit Tests for the Floyd Warshall function


# Import floyd function
from main import floyd

# Import test cases
from test_cases import (sample_a, sample_b,
                        output_a, output_b)

# Import testing package
import unittest

# Unit Tests
class TestFloyd(unittest.TestCase):

    def test_floyd_a(self):
        self.assertEqual(floyd(sample_a), output_a, "Output incorrect")

    def test_floyd_b(self):
        self.assertEqual(floyd(sample_b), output_b, "Output incorrect")


if __name__ == '__main__':
    unittest.main()
