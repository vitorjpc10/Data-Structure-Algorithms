#! https://leetcode.com/problems/two-sum/
"""
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution(object):

    def twoSumBruteForce(self, nums, target):
        """
        Find the indices of two numbers in the given list that add up to the target using a brute-force approach.

        Args:
            nums (List[int]): The list of integers.
            target (int): The target sum.

        Returns:
            List[int]: The indices of the two numbers that add up to the target, or an empty list if no solution is found.

        """
        # Iterate through each number in the list
        for i in range(len(nums)):
            # Iterate through the remaining numbers after the current number
            for j in range(i + 1, len(nums)):

                # Check if the sum of the two numbers equals the target
                if nums[i] + nums[j] == target:

                    # Return the indices of the two numbers
                    return [i, j]

        # If no solution is found, return an empty list
        return []

    def twoSumSingleLoop(self, nums, target):
        """
        Find the indices of two numbers in the given list that add up to the target using a single loop approach.

        Args:
            nums (List[int]): The list of integers.
            target (int): The target sum.

        Returns:
            List[int]: The indices of the two numbers that add up to the target, or an empty list if no solution is found.

        """
        # Iterate through each number in the list
        for i in range(len(nums)):

            # Calculate the complement of the current number
            complement = target - nums[i]

            # Check if the complement exists in the list and is not the same element
            if complement in nums and nums.index(complement) != i:
                # Return the indices of the two numbers
                return [i, nums.index(complement)]

        # If no solution is found, return an empty list
        return []

    def twoSumDictionary(self, nums, target):

        # Create a dictionary to store the complement of each element
        complement_dict = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement of the current element
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in complement_dict:
                # Return the indices of the two numbers that add up to the target
                return [complement_dict[complement], i]

            # Add the current element and its index to the dictionary
            complement_dict[num] = i

        # If no solution is found, return an empty list or raise an exception
        return []


obj = Solution()

nums1 = [2, 7, 11, 15, 3, 6]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6

print("Brute force:")
print(obj.twoSumBruteForce(nums1, target1))
print(obj.twoSumBruteForce(nums2, target2))
print(obj.twoSumBruteForce(nums3, target3))

print("\n====================\n")

print("Single loop:")
print(obj.twoSumSingleLoop(nums1, target1))
print(obj.twoSumSingleLoop(nums2, target2))
print(obj.twoSumSingleLoop(nums3, target3))

print("\n====================\n")

print("Dictionary:")
print(obj.twoSumDictionary(nums1, target1))
print(obj.twoSumDictionary(nums2, target2))
print(obj.twoSumDictionary(nums3, target3))
