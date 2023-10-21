#! https://leetcode.com/problems/valid-palindrome/
"""
125. Valid Palindrome
Easy
8.4K
8K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        Checks if a given string is a palindrome.

        :param s: The input string to check.
        :type s: str
        :return: True if the string is a palindrome, False otherwise.
        :rtype: bool

        Time Complexity: O(n)
        - The time complexity of this method is O(n), where n is the length of the cleaned string.
        - This is because the method iterates over the cleaned string once in the while loop.

        Space Complexity: O(1)
        - The space complexity of this method is O(1), as it does not use any additional data structures that scale with the input size.
        """

        # Initialize the left and right pointers
        i = 0
        j = len(s) - 1

        # Compare characters at each position from the start and end of the cleaned string
        while i < j:

            # Skip non-alphanumeric characters from the left side of the string
            if not s[i].isalnum():
                i += 1
                continue

            # Skip non-alphanumeric characters from the right side of the string
            if not s[j].isalnum():
                j -= 1
                continue

            # If the characters at the current positions do not match, the string is not a palindrome
            if s[i].lower() != s[j].lower():
                return False

            # Move the pointers towards each other
            i += 1
            j -= 1

        # If all characters matched, or the pointers crossed each other, the string is a palindrome
        return True




obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
print(obj.isPalindrome("race a car"))
print(obj.isPalindrome(" "))
