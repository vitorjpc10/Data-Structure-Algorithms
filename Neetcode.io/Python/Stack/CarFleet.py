#! https://leetcode.com/problems/car-fleet/
"""
853. Car Fleet
Medium
3.1K
744
Companies
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.



Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        Calculate the number of car fleets that will arrive at the destination.

        Args:
            target (int): The destination point.
            position (List[int]): List of positions of the cars.
            speed (List[int]): List of speeds of the cars.

        Returns:
            int: The number of car fleets that will arrive at the destination.

        """

        # Combine the position and speed lists into a list of tuples
        cars = list(zip(position, speed))

        # Sort the cars based on their positions in descending order (furthest car from starting point comes first)
        cars.sort(reverse=True, key=lambda x: x[0])

        # Initialize the number of fleets to 0 (in other words the num of fleets is seperated by the group of cars)
        fleets = 0

        # Initialize the maximum time to reach the destination to 0 (maximum fastest car to reach target position)
        max_time = 0

        for car in cars:
            # Calculate the time taken for the current car to reach the destination
            time = float(target - car[0]) / car[1]

            # If the current car takes more time to reach the destination than the maximum time,
            # it means a new fleet is formed
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets

obj = Solution()
print(obj.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
print(obj.carFleet(target = 10, position = [3], speed = [3]))
print(obj.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))