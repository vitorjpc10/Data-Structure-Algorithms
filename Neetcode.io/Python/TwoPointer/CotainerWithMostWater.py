#! https://leetcode.com/problems/container-with-most-water/
"""
11. Container With Most Water
Medium
27.1K
1.5K
Companies
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

class Solution(object):
    def maxArea(self, height):
        """
        Finds the maximum area of water that can be contained between two vertical lines.

        :param height: The list of heights of the vertical lines.
        :type height: List[int]
        :return: The maximum area of water.
        :rtype: int

        Time Complexity: O(n)
        - The method uses a two-pointer technique to find the maximum area.
        - The two pointers, `i` and `j`, start from the two ends of the list.
        - The pointers move towards each other until they meet in the middle.
        - The method only iterates through the list once, so the time complexity is O(n), where n is the length of the list.
        - As the input size increases, the time taken by this method grows linearly.

        Space Complexity: O(1)
        - The method uses a constant amount of extra space to store the maximum area, `maxArea`.
        - It does not use any additional data structures that scale with the input size.
        - Therefore, the space complexity is O(1), indicating constant space usage.
        - As the input size increases, the space taken by this method remains constant.
        """

        maxArea = 0

        i = 0
        j = len(height) - 1

        while i < j:
            # Calculate the current area and update the maximum area if necessary
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))

            # Move the pointer with the smaller height towards the other pointer
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea


obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))