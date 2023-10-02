#! https://leetcode.com/problems/group-anagrams/
"""
49. Group Anagrams
Medium
17.3K
508
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

class Solution(object):
    def groupAnagramsDictionary(self, strs):
        """
        Groups anagrams in a given list of strings.

        Args:
            strs (List[str]): The list of strings to group anagrams.

        Returns:
            List[List[str]]: A list of lists, where each inner list contains anagrams of each other.

        """

        # Create a dictionary to store the anagram groups
        sorted_anagram_dict = {}

        # Iterate through each word in the input list
        for word in strs:
            # Sort the letters of the word and convert it to a string
            sorted_word = str(sorted(word))

            # Check if the sorted word exists as a key in the dictionary
            if sorted_word in sorted_anagram_dict:
                # If it does, append the current word to the existing anagram group
                sorted_anagram_dict[sorted_word].append(word)
            else:
                # If it does not, create a new anagram group with the current word
                sorted_anagram_dict[sorted_word] = [word]

        # Return the values of the dictionary as a list of anagram groups
        return list(sorted_anagram_dict.values())

obj = Solution()

print(obj.groupAnagramsDictionary(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(obj.groupAnagramsDictionary([""]))
print(obj.groupAnagramsDictionary(["a"]))