from typing import List
import unittest

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
class TestContainsDuplicate(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_with_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_without_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test_single_element(self):
        self.assertFalse(self.solution.containsDuplicate([1]))

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_all_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([5, 5, 5, 5]))

    def test_large_input_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate(list(range(1000000))))

    def test_large_input_with_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate(list(range(1000000)) + [0]))

if __name__ == '__main__':
    unittest.main()
