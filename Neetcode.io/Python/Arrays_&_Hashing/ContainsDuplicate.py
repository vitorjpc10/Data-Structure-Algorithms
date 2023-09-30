#! https://leetcode.com/problems/contains-duplicate/
"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution(object):
    def containsDuplicateSet(self, nums):
       """
       Check if a list contains duplicate elements using a set.
   
       Args:
           nums (List[int]): The list of integers to check for duplicates.
   
       Returns:
           bool: True if the list contains duplicates, False otherwise.
       """
       # Create a set from the list
       nums_set = set(nums)
       
       # Check if the length of the list is equal to the length of the set
       # If they are not equal, it means there are duplicate elements in the list
       return len(nums) != len(nums_set)

    def containsDuplicateDictionary(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_count_dict = {}  # Create an empty dictionary to store number counts
        
        for num in nums:
            if num in num_count_dict:
                return True  # If the number is already in the dictionary, return True
            else:
                # If the number is not in the dictionary, assume a count of 0,
                # add 1 to it, and then update the dictionary with the new count
                num_count_dict[num] = num_count_dict.get(num, 0) + 1
            
        return False  # If the loop completes without finding a duplicate, return False

        
solution = Solution()

list = [1,2,3,1]
list2 = [1,2,3,4]
list3 = [1,1,1,3,3,4,3,2,4,2]

print("Dictionary:")
print(solution.containsDuplicateDictionary(list))
print(solution.containsDuplicateDictionary(list2))
print(solution.containsDuplicateDictionary(list3))

print("\n================================\n")

print("Set:")
print(solution.containsDuplicateSet(list))
print(solution.containsDuplicateSet(list2))
print(solution.containsDuplicateSet(list3))






