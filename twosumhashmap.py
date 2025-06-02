from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List [int]:
        prevMap = {} #value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
def run_tests():
    sol = Solution()

    # Each test prints the result and whether it passed

    # Test Case 1: Basic test
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = sol.twoSum(nums1, target1)
    print("Test 1:", "Passed" if result1 == expected1 else f"Failed (Got {result1})")

    # Test Case 2: Different numbers
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = sol.twoSum(nums2, target2)
    print("Test 2:", "Passed" if result2 == expected2 else f"Failed (Got {result2})")

    # Test Case 3: Duplicates
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = sol.twoSum(nums3, target3)
    print("Test 3:", "Passed" if result3 == expected3 else f"Failed (Got {result3})")

    # Test Case 4: No solution
    nums4 = [1, 2, 3, 4]
    target4 = 8
    expected4 = []
    result4 = sol.twoSum(nums4, target4)
    print("Test 4:", "Passed" if result4 == expected4 else f"Failed (Got {result4})")

    # Test Case 5: Negative numbers
    nums5 = [-1, -2, -3, -4, -5]
    target5 = -8
    expected5 = [2, 4]
    result5 = sol.twoSum(nums5, target5)
    print("Test 5:", "Passed" if result5 == expected5 else f"Failed (Got {result5})")

# Run the tests when the file is executed
if __name__ == "__main__":
    run_tests()