from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
def run_tests():
    sol = Solution()

    # Test case 1
    print(sol.twoSum([2, 7, 11, 15], 9))  # Expected: [1, 2]

    # Test case 2
    print(sol.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # Expected: [4, 5]

    # Test case 3
    print(sol.twoSum([-1, 0], -1))  # Expected: [1, 2]

    # Test case 4
    print(sol.twoSum([1, 3, 4, 5, 7, 10, 11], 9))  # Expected: [3, 5]

    # Test case 5
    print(sol.twoSum([1, 2], 3))  # Expected: [1, 2]
    
if __name__ == "__main__":
    run_tests()
#This means run the test cases only if you're executing the file directly in VS Code or terminal.

#If this file is imported somewhere else (e.g., into a unit test framework), it won’t accidentally run run_tests() on import.
#time complexity O(n), space complexity O(1)