#! https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
84. Largest Rectangle in Histogram
Hard
16K
230
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        Calculates the area of the largest rectangle in the histogram.

        :param heights: List of integers representing the heights of the histogram bars.
        :return: The area of the largest rectangle in the histogram.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Initialize variables
        stack = []  # Stack to store the indices of bars in non-decreasing order of heights
        max_area = 0  # Variable to store the maximum area of a rectangle

        # Iterate through each bar in the histogram
        for i in range(len(heights)):
            # Check if the current bar is smaller than the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                # Calculate the area of the rectangle formed by the bar at the top of the stack
                # and the bars to the left and right of it
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = height * width

                # Update the maximum area if necessary
                max_area = max(max_area, area)

            # Add the current bar's index to the stack
            stack.append(i)

        # Process the remaining bars in the stack
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)

        return max_area


obj = Solution()
print(obj.largestRectangleArea([2,1,5,6,2,3]))
print(obj.largestRectangleArea([2,4]))