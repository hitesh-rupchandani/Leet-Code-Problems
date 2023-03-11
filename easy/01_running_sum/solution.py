"""
    Running Sum of 1d Array

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    
    Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
    
    Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]
"""

from typing import List

class Solution:
    """
    Solution class for Running Sum of 1d Array.
    """

    def running_sum_1(self, nums: List[int]) -> List[int]:
        """
            Solution 1 :  Time complexity: O(n) and Space complexity: O(1)
        """

        sums = [nums[0]]
        for num in nums[1:]:
            sums.append(sums[-1] + num)
        return sums

    def running_sum_2(self, nums: List[int]) -> List[int]:
        """
            Solution 2 :  Time complexity: O(n) and Space complexity: O(1)
        """

        for index in range(1,len(nums)):
            nums[index] += nums[index -1]
        return nums

def main() -> None:
    """
        This is main method or driver method
    """
    
    solution = Solution()
    print("Solution 1")
    print(solution.running_sum_1(nums=[1,2,3,4]))
    print(solution.running_sum_1(nums=[1,1,1,1,1]))
    print(solution.running_sum_1(nums=[3,1,2,10,1]))

    print("Solution 2")
    print(solution.running_sum_2(nums=[1,2,3,4]))
    print(solution.running_sum_2(nums=[1, 1, 1, 1, 1]))
    print(solution.running_sum_2(nums=[3,1,2,10,1]))

if __name__ == "__main__":
    main()
