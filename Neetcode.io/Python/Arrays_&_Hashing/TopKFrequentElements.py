#! https://leetcode.com/problems/top-k-frequent-elements/
"""
347. Top K Frequent Elements
Medium
16.1K
578
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Returns the top k frequent elements in the given list of numbers.

        :param nums: List[int] - The input list of numbers.
        :param k: int - The number of top frequent elements to be returned.
        :return: List[int] - The list of top k frequent elements.

        Algorithm:
        1. Create a dictionary, num_count_dict, to store the count of each number in nums.
        2. Iterate over each number in nums:
           - If the number is already present in num_count_dict, increment its count by 1.
           - If the number is not present, add it to num_count_dict with a count of 1.
        3. Sort the items of num_count_dict based on their counts in descending order.
        4. Extract the first k elements from the sorted list of tuples and store them in sorted_num_count_dict.
        5. Create an empty list, result.
        6. Iterate over each num_count tuple in sorted_num_count_dict:
           - Append the first element (the number) of the tuple to the result list.
        7. Return the result list.
        """

        # Step 1: Create a dictionary to store the count of each number
        num_count_dict = {}

        # Step 2: Count the frequency of each number
        for num in nums:
            if num in num_count_dict:
                num_count_dict[num] += 1
            else:
                num_count_dict[num] = 1

        # Step 3: Sort the dictionary items based on their counts in descending order
        sorted_num_count_dict = sorted(num_count_dict.items(), key=lambda x: x[1], reverse=True)

        # Step 4: Extract the first k elements from the sorted list
        result = []
        for num_count in sorted_num_count_dict[0:k]:
            result.append(num_count[0])

        # Step 7: Return the list of top k frequent elements
        return result





obj = Solution()

nums = [2,2,3,1,1,1]
k = 2
nums1 = [1]
k1 = 1
nums2 = []
k2 = 1

print(obj.topKFrequent(nums, k))
print(obj.topKFrequent(nums1, k1))
print(obj.topKFrequent(nums2, k2))
