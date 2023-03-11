"""
    Richest Customer Wealth

    Example 1:
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    Explanation:
        1st customer has wealth = 1 + 2 + 3 = 6
        2nd customer has wealth = 3 + 2 + 1 = 6
        Both customers are considered the richest with a wealth of 6 each, so return 6.
     
    Example 2:
    Input: accounts = [[1,5],[7,3],[3,5]]
    Output: 10
    Explanation: 
        1st customer has wealth = 6
        2nd customer has wealth = 10 
        3rd customer has wealth = 8
        The 2nd customer is the richest with a wealth of 10.

    
    Example 3:
    Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
    Output: 17
"""

from typing import List

class Solution:
    """
    Solution class for Richest Customer Wealth
    """

    def maximum_wealth_1(self, accounts: List[List[int]]) -> int:
        """
            Time complexity:  and Space complexity: 
        """

        max_wealth = [sum(accounts[0])]
        _ = [max_wealth.insert(0, sum(money)) for money in accounts[1:] if sum(money) > max_wealth[0]]
        return max(max_wealth)

    def maximum_wealth_2(self, accounts: List[List[int]]) -> int:
        """
            Time complexity: O(n) and Space complexity: O(1)
        """
        return max([sum(money) for money in accounts])

def main() -> None:
    """
        This is main method or driver method
    """

    solution = Solution()
    print("Solution 1")
    print(solution.maximum_wealth_1(accounts=[[1,2,3],[3,2,1]]))
    print(solution.maximum_wealth_1(accounts=[[1,5],[7,3],[3,5]]))
    print(solution.maximum_wealth_1(accounts=[[2,8,7],[7,1,3],[1,9,5]]))

    print("Solution 2")
    print(solution.maximum_wealth_2(accounts=[[1,2,3],[3,2,1]]))
    print(solution.maximum_wealth_2(accounts=[[1,5],[7,3],[3,5]]))
    print(solution.maximum_wealth_2(accounts=[[2,8,7],[7,1,3],[1,9,5]]))

if __name__ == "__main__":
    main()
