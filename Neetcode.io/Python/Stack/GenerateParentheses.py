#! https://leetcode.com/problems/generate-parentheses/
"""
22. Generate Parentheses
Medium
19.8K
811
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        Generate all combinations of well-formed parentheses.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            List[str]: A list of all combinations of well-formed parentheses.

        """

        def backtrack(result, current, open_parentheses_count, close_parentheses_count, max_pairs):
            """
            Recursive helper function to generate all combinations of well-formed parentheses.

            Args:
                result (List[str]): The list to store the resulting combinations.
                current (str): The current combination string.
                open_parentheses_count (int): The count of open parentheses in the current combination.
                close_parentheses_count (int): The count of close parentheses in the current combination.
                max_pairs (int): The maximum number of pairs of parentheses.

            Returns:
                None

            """

            # Base case: if the current string has the desired length
            if len(current) == max_pairs * 2:
                result.append(current)
                return

            # If we can add an opening parenthesis, do so
            if open_parentheses_count < max_pairs:
                backtrack(result, current + "(", open_parentheses_count + 1, close_parentheses_count, max_pairs)

            # If we can add a closing parenthesis, do so
            if close_parentheses_count < open_parentheses_count:
                backtrack(result, current + ")", open_parentheses_count, close_parentheses_count + 1, max_pairs)

        result = []  # Initialize the result list
        backtrack(result, "", 0, 0, n)  # Call the backtrack function to generate combinations
        return result



obj = Solution()
print(obj.generateParenthesis(2))