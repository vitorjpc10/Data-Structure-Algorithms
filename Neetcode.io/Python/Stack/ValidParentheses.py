#! https://leetcode.com/problems/valid-parentheses/
"""
20. Valid Parentheses
Easy
22.3K
1.5K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
class Solution(object):
    def isValid(self, s):
        """
        Determines if a given string of parentheses, brackets, and curly braces is valid.

        :param s: str - The input string.
        :return: bool - True if the string is valid, False otherwise.

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(n), where n is the length of the input string.
        """

        stack = []

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)

            if char in [')', ']', '}']:
                if not stack:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                stack.pop()

        if len(stack) != 0:
            return False
        else:
            return True


    def isValidDictionary(self, s):
        """
        Determines if a given string of parentheses, brackets, and curly braces is valid.

        :param s: str - The input string.
        :return: bool - True if the string is valid, False otherwise.

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(n), where n is the length of the input string.
        """

        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False

        return len(stack) == 0





obj = Solution()

s = "()"
s1 = "()[]{}"
s2 = "(]"

print(obj.isValid(s))
print(obj.isValid(s1))
print(obj.isValid(s2))

print("\n=================================\n")

print(obj.isValidDictionary(s))
print(obj.isValidDictionary(s1))
print(obj.isValidDictionary(s2))
