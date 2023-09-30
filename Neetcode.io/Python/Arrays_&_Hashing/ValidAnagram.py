#! https://leetcode.com/problems/valid-anagram/description/
"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution:

    def isAnagramSorted(self, s, t):

        """
        Check if two strings are anagrams by sorting them and comparing the sorted versions.

        Args:
            s: The first string.
            t: The second string.

        Returns:
            True if the strings are anagrams, False otherwise.
        """

        # Check if the strings have different lengths
        if len(s) != len(t):
            return False

        # Sort the strings
        word1 = sorted(s)
        word2 = sorted(t)

        # Compare the sorted strings
        return word1 == word2

    def isAnagramDictionary(self, s, t):
        """
        Check if two strings are anagrams using dictionaries.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """

        s_dictionary = {}
        t_dictionary = {}

        # Count the frequency of each character in s
        for char in s:
            s_dictionary[char] = s_dictionary.get(char, 0) + 1

        # Count the frequency of each character in t
        for char in t:
            t_dictionary[char] = t_dictionary.get(char, 0) + 1

        # Check if the dictionaries are equal
        return s_dictionary == t_dictionary


obj = Solution()

print("Sorted")
print(obj.isAnagramSorted("anagram", "nagaram"))
print(obj.isAnagramSorted("rat", "car"))

print("\n==================================\n")

print("Dictionary")
print(obj.isAnagramDictionary("anagram", "nagaram"))
print(obj.isAnagramDictionary("rat", "car"))
