#! https://leetcode.com/problems/3sum/
'''
15. 3Sum
Medium
28.9K
2.6K
Companies
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''

class Solution(object):
    def threeSum(self, nums):
        """
        Finds all unique triplets in the given list that add up to zero.

        :param nums: The list of numbers.
        :type nums: List[int]
        :return: The list of unique triplets.
        :rtype: List[List[int]]

        Time Complexity: O(n^2)
        - The method uses a two-pointer technique to find the second and third numbers of the triplet.
        - The outer loop runs n-2 times, and the inner loop runs n-1, n-2, ..., 2, or 1 times.
        - Therefore, the total number of iterations is roughly (n-2) + (n-3) + ... + 2 + 1 = (n-2)*(n-1)/2, which is roughly O(n^2).
        - As the input size increases, the time taken by this method grows quadratically.

        Space Complexity: O(n)
        - The method uses a list to store the result, which can have at most n/3 triplets.
        - Therefore, the space complexity is O(n/3), which is equivalent to O(n).
        - As the input size increases, the space taken by this method grows linearly.
        """

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            leftPointer = i + 1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                threeSum = nums[i] + nums[leftPointer] + nums[rightPointer]

                if threeSum == 0:
                    result.append([nums[i], nums[leftPointer], nums[rightPointer]])

                    # Skip duplicates for the second number
                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer + 1]:
                        leftPointer += 1
                    leftPointer += 1

                    # Skip duplicates for the third number
                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer - 1]:
                        rightPointer -= 1
                    rightPointer -= 1

                elif threeSum < 0:
                    leftPointer += 1
                else:
                    rightPointer -= 1

        return result



obj = Solution()

print(obj.threeSum([-1,0,1,2,-1,-4]))
print(obj.threeSum([0,1,1]))
print(obj.threeSum([0,0,0]))
