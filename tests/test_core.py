import unittest
from flatten_utils.core import deep_flatten

class TestFlatten(unittest.TestCase):
    def test_flat_list(self):
        data = [1, [2, [3, 4], 5], 6]
        result = list(deep_flatten(data))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_depth_limit(self):
        data = [1, [2, [3, 4]]]
        result = list(deep_flatten(data, depth=2))
        self.assertEqual(result, [1, 2, 3, [4]])

    def test_string_is_not_flattened(self):
        data = ["hello", ["world"]]
        result = list(deep_flatten(data))
        self.assertEqual(result, ["hello", "world"])

if __name__=="__main__":
    unittest.main()