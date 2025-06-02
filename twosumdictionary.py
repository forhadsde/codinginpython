from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []
    
    # Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    print("Test 1:", sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]

    # Test Case 2
    print("Test 2:", sol.twoSum([3, 2, 4], 6))  # Expected: [1, 2]

    # Test Case 3
    print("Test 3:", sol.twoSum([3, 3], 6))  # Expected: [0, 1]

    # Test Case 4
    print("Test 4:", sol.twoSum([1, 2, 3, 4], 8))  # Expected: []
