#! https://leetcode.com/problems/product-of-array-except-self/
"""
238. Product of Array Except Self
Medium
20.1K
1.2K
Companies
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
class Solution(object):
    def productExceptSelfBruteForce(self, nums):
        """
        Returns an array where each element at index i is the product of all elements in the input list `nums` except the element at index i.

        :param nums: List[int] - The input list of integers.
        :return: List[int] - The list of products of all elements except self.

        Algorithm:
        1. Create an empty list, `result`, to store the products.
        2. Iterate over each element in `nums` using the index `i`:
           - Set the initial product to 1.
           - Iterate over each element in `nums` using the index `j`:
             - If `i` is not equal to `j`, multiply the product by `nums[j]`.
           - Append the product to the `result` list.
        3. Return the `result` list.

        Time complexity: O(n^2)
        Space complexity: O(n)
        """

        result = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            result.append(product)

        return result

    def productExceptSelfOofN(self, nums):
        """
        Returns an array where each element at index i is the product of all elements in the input list `nums` except the element at index i.

        :param nums: List[int] - The input list of integers.
        :return: List[int] - The list of products of all elements except self.

        Algorithm:
        1. Create an array `result` of length `n` and initialize it with 1.
        2. Iterate over `nums` from left to right:
           - Store the product of all elements to the left of the current element in `result[i]`.
           - Update the `prefix` value by multiplying it with the current element.
        3. Iterate over `nums` from right to left:
           - Multiply the product of all elements to the right of the current element with the corresponding element in `result`.
           - Update the `postfix` value by multiplying it with the current element.
        4. Return the `result` array.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            # Store the product of all elements to the left of the current element
            result[i] = prefix
            # Update the prefix value by multiplying it with the current element
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            # Multiply the product of all elements to the right of the current element with the corresponding element in `result`
            result[i] *= postfix
            # Update the postfix value by multiplying it with the current element
            postfix *= nums[i]

        return result

#todo: Watch a tutorial on this question
#! https://www.youtube.com/watch?v=bNvIQI2wAjk


obj = Solution()

nums = [1,2,3,4]
nums1 = [-1,1,0,-3,3]

print(obj.productExceptSelfBruteForce(nums))
print(obj.productExceptSelfBruteForce(nums1))

print("\n==================================================================\n")

print(obj.productExceptSelfOofN(nums))
print(obj.productExceptSelfOofN(nums1))