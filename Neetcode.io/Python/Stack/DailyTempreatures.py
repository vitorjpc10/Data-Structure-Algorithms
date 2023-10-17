#! https://leetcode.com/problems/daily-temperatures/
"""
739. Daily Temperatures
Medium
11.8K
257
Companies
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

"""

class Solution(object):
    def dailyTemperaturesBruteForce(self, temperatures):
        """
        Find the number of days you have to wait until a warmer temperature for each day.

        Args:
            temperatures (List[int]): List of daily temperatures.

        Returns:
            List[int]: List of the number of days you have to wait until a warmer temperature for each day.

        Time Complexity:
            O(n^2), where n is the length of the `temperatures` list. This is because we have nested loops, and in the worst case, we iterate over all pairs of days.

        Space Complexity:
            O(n), where n is the length of the `temperatures` list. This is because we create a new list, `result`, to store the result, which has the same length as the `temperatures` list.

        """

        result = [0] * len(temperatures)  # Initialize a list to store the result

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:  # If a warmer temperature is found
                    result[i] = j - i  # Store the number of days until a warmer temperature
                    break

        return result

    def dailyTemperaturesMonotonicStack(self, temperatures):
        """
        Find the number of days you have to wait until a warmer temperature for each day.

        Args:
            temperatures (List[int]): List of daily temperatures.

        Returns:
            List[int]: List of the number of days you have to wait until a warmer temperature for each day.

        Time Complexity:
            O(n), where n is the length of the `temperatures` list. We iterate through the temperature list once.

        Space Complexity:
            O(n), where n is the length of the `temperatures` list. We use a stack to store indices of temperatures.

        """

        stack = []  # Initialize a stack to store indices of temperatures
        result = [0] * len(temperatures)  # Initialize a list to store the result

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:  # If a cooler temperature is found
                index = stack.pop()  # Get the index of the previous temperature
                result[index] = i - index  # Calculate the number of days until a warmer temperature

            stack.append(i)  # Add the current index to the stack

        return result



obj = Solution()

temperatures = [73,74,75,71,69,72,76,73]
temperatures1 = [30,40,50,60]
temperatures2 = [30,60,90]

print(obj.dailyTemperaturesBruteForce(temperatures))
print(obj.dailyTemperaturesBruteForce(temperatures1))
print(obj.dailyTemperaturesBruteForce(temperatures2))

print("\n================================\n")

print(obj.dailyTemperaturesMonotonicStack(temperatures))
print(obj.dailyTemperaturesMonotonicStack(temperatures1))
print(obj.dailyTemperaturesMonotonicStack(temperatures2))
