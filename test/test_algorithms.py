import unittest
import random
from searchArray import algorithms


def generate_data(size, min_val, max_val):
    return sorted([random.randint(min_val, max_val) for _ in range(size)])


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.data = generate_data(20, 1, 100)
        self.existing_value = random.choice(self.data)
        self.non_existing_value = max(self.data) + 1

    def test_linear_search(self):
        self.assertNotEqual(algorithms.linear_search(self.data, self.existing_value), -1)
        self.assertEqual(algorithms.linear_search(self.data, self.non_existing_value), -1)

    def test_binary_search(self):
        self.assertNotEqual(algorithms.binary_search(self.data, self.existing_value), -1)
        self.assertEqual(algorithms.binary_search(self.data, self.non_existing_value), -1)

    def test_ternary_search(self):
        self.assertNotEqual(algorithms.ternary_search(self.data, self.existing_value), -1)
        self.assertEqual(algorithms.ternary_search(self.data, self.non_existing_value), -1)

    def test_jump_search(self):
        self.assertNotEqual(algorithms.jump_search(self.data, self.existing_value), -1)
        self.assertEqual(algorithms.jump_search(self.data, self.non_existing_value), -1)

    def test_interpolation_search(self):
        self.assertNotEqual(algorithms.interpolation_search(self.data, self.existing_value), -1)
        self.assertEqual(algorithms.interpolation_search(self.data, self.non_existing_value), -1)


if __name__ == "__main__":
    unittest.main()
