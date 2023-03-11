"""
    Find Pivot Index

    Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:The pivot index is 3.
                Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
                Right sum = nums[4] + nums[5] = 5 + 6 = 11
     
    Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:There is no index that satisfies the conditions in the problem statement.
    
    Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:The pivot index is 0.
                Left sum = 0 (no elements to the left of index 0)
                Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""

from typing import List

class Solution:
    """
    Solution class for find pivot index.
    """

    def pivot_index(self, nums: List[int]) -> int:
        """
            Time complexity: O(n) and Space complexity: O(1)
        """

        total = sum(nums)
        left_sum = 0
        for index, value in enumerate(nums):
            if left_sum == (total - nums[index] - left_sum):
                return index
            left_sum += value
        return -1

def main() -> None:
    """
        This is main method or driver method
    """
    
    solution = Solution()
    print(solution.pivot_index(nums=[1,7,3,6,5,6]))
    print(solution.pivot_index(nums=[1,2,3]))
    print(solution.pivot_index(nums=[2,1,-1]))

if __name__ == "__main__":
    main()
