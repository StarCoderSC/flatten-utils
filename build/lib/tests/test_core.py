import unittest
from flatten_utils.core import deep_flatten, flatten_limited

class TestFlatten(unittest.TestCase):
    
    def test_flat_list(self):
        data = [1, [2, [3, 4], 5], 6]
        result = list(deep_flatten(data))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_depth_limit(self):
        data = [1, [2, [3, [4]]]]
        result = list(flatten_limited(data, depth=2))
        self.assertEqual(result, [1, 2, [3, [4]]])

    def test_stop_at_str(self):
        data = ["hello", ["world"]]
        result = list(deep_flatten(data))
        self.assertEqual(result, ["hello", "world"])

    def test_stop_at_dict(self):
        data = {"a": 1, "b": {"c": 2}}
        result = list(deep_flatten(data, stop_at=(dict,)))
        self.assertEqual(result, [data])

    def test_flatten_limited_with_stop_at(self):
        data = [{"x": 1}, {"y": [2, 3]}]
        result = list(flatten_limited(data, depth=2, stop_at=(dict,)))
        self.assertEqual(result, [{"x": 1}, {"y": [2, 3]}])

    def test_empty_input(self):
        result = list(deep_flatten([]))
        self.assertEqual(result, [])

    def test_non_iterable_input(self):
        result = list(deep_flatten(42))
        self.assertEqual(result, [42])

    def test_deep_flatten_generator_behavior(self):
        data = (x for x in [1, [2, [3]]])  # generator input
        result = list(deep_flatten(data))
        self.assertEqual(result, [1, 2, 3])

    def test_mixed_types(self):
        data = [1, "hello", {"key": [2, 3]}, (4, 5)]
        result = list(deep_flatten(data))
        self.assertEqual(result, [1, "hello", "key", 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
