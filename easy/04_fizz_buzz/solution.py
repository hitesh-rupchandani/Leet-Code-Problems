"""
    Fizz Buzz

    Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]
     
    Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]
    
    Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

from typing import List

class Solution:
    """
    Solution class for Fizz Buzz game.
    """

    def fizz_buzz(self, number: int) -> List[str]:
        """
            fizz_buzz
        """
        answer = []
        for num in range(1,number+1):
            if num % 3 == 0 and num % 5 == 0
                answer.append("FizzBuzz")
            elif num % 3 == 0:
                answer.append("Fizz")
            elif num % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(num))
        return answer

def main() -> None:
    """
        This is main method or driver method
    """
    
    solution = Solution()
    print(solution.fizz_buzz(n=3))
    print(solution.fizz_buzz(n=5))
    print(solution.fizz_buzz(n=15))

if __name__ == "__main__":
    main()
