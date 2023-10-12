#! https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
150. Evaluate Reverse Polish Notation
Medium
6.6K
962
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        Evaluates the given Reverse Polish Notation (RPN) expression.

        Args:
            tokens (List[str]): The RPN expression as a list of tokens.

        Returns:
            int: The result of evaluating the RPN expression.

        Raises:
            None

        Example:
            tokens = ["2", "1", "+", "3", "*"]
            result = evalRPN(tokens)
            print(result)  # Output: 9

        Complexity Analysis:
        Time complexity: O(n), where n is the number of tokens in the expression.
            The algorithm iterates through each token in the expression once.

        Space complexity: O(n), where n is the number of tokens in the expression.
            The algorithm uses a stack to store the numbers, which can grow up to the size of the expression.
            Additionally, the algorithm uses some extra space to store the intermediate results during evaluation.
        """

        # Create an empty stack to store the numbers
        num_stack = []

        # Iterate over the tokens in the expression
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # If the token is an operator, pop the top two numbers from the stack
                operand2 = num_stack.pop()
                operand1 = num_stack.pop()

                # Create an expression string using the operands and the current operator
                expression = "{operand1} {operator} {operand2}"

                # Evaluate the expression using eval and format the string with the operands and operator
                calc = int(eval(expression.format(operand1=operand1, operator=token, operand2=operand2)))

                # Push the result of the evaluation back onto the stack
                num_stack.append(calc)
            else:
                # If the token is a number, convert it to an integer and push it onto the stack
                num_stack.append(int(token))

        # The final result of the expression will be at the top of the stack
        return num_stack.pop()



obj = Solution()
print(obj.evalRPN(["2","1","+","3","*"]))
print(obj.evalRPN(["4","13","5","/","+"]))
print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))