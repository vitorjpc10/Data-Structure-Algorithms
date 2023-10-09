#! https://leetcode.com/problems/longest-consecutive-sequence/
"""
128. Longest Consecutive Sequence
Medium
18.4K
833
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution(object):
    def longestConsecutiveBruteForce(self, nums):
        """
        Finds the length of the longest consecutive subsequence in a given list of integers using a brute-force approach.

        :param nums: List[int] - The input list of integers.
        :return: int - The length of the longest consecutive subsequence.

        Time complexity: O(n log n), where n is the length of the input list.
        Space complexity: O(1).

        Note: This implementation assumes that the input list contains no duplicates.
        """

        # Check if the input list is empty
        if len(nums) == 0:
            return 0

        # Sort the input list in ascending order
        sorted_nums = sorted(nums)

        longest = 0
        current_longest = 0
        for i in range(len(sorted_nums) - 1):

            # Skip duplicates
            if sorted_nums[i] == sorted_nums[i+1]:
                continue

            # Increment the current longest length if the next number is consecutive
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                current_longest += 1
            else:
                # Update the longest length and reset the current longest length
                longest = max(longest, current_longest)
                current_longest = 0

        # Return the maximum of the longest length and the current longest length plus 1 (initial consecutive number is inclusive)
        return max(longest, current_longest) + 1

    def longestConsecutive(self, nums):
        """
        Finds the length of the longest consecutive elements sequence in a given unsorted array of integers.

        :param nums: List[int] - The input list of integers.
        :return: int - The length of the longest consecutive elements sequence.

        Time complexity: O(n), where n is the length of the input array.
        Space complexity: O(n), where n is the length of the input array.
        """

        # Step 1: Create a set to store all the numbers in the input array
        num_set = set(nums)

        longest_length = 0

        # Step 2: Iterate through the input array
        for num in num_set:
            # Step 4: Check if the number minus 1 exists in the set
            if num - 1 not in num_set:
                current_length = 1

                # Step 5: Iterate through the consecutive sequence
                while num + 1 in num_set:
                    num += 1
                    current_length += 1

                # Step 6: Update the longest length if necessary
                longest_length = max(longest_length, current_length)

        # Step 7: Return the longest length
        return longest_length






obj = Solution()
input = [100,4,200,1,3,2]
input1 = [0,3,7,2,5,8,4,6,0,1]
input3 = [9,1,4,7,3,-1,0,5,8,-1,6]

print(obj.longestConsecutiveBruteForce(input))
print(obj.longestConsecutiveBruteForce(input1))
print(obj.longestConsecutiveBruteForce(input3))

print("\n================================\n")

print(obj.longestConsecutive(input))
print(obj.longestConsecutive(input1))
print(obj.longestConsecutive(input3))