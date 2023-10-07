#! https://www.lintcode.com/problem/659/
"""
659 · Encode and Decode Strings
Algorithms
Medium
Accepted Rate
65%
Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""
class Solution:
    def encode(self, strs):
        """
        Encodes a list of strings by concatenating them with the ":;" delimiter.

        :param strs: List[str] - The input list of strings to encode.
        :return: str - The encoded string.

        Time complexity: O(n), where n is the total length of the input strings.
        Space complexity: O(n), where n is the total length of the input strings.
        """

        # Initialize an empty string to store the encoded string
        encoded_string = ""

        # Iterate over each word in the input list
        for word in strs:
            # Concatenate the word with the ":;" delimiter
            encoded_string += word + ":;"

        return encoded_string


    def decode(self, str):
        """
        Decodes a string by splitting it at each occurrence of the ":;" delimiter.

        :param str: str - The input string to decode.
        :return: List[str] - The decoded string as a list of substrings.

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(n), where n is the length of the input string.
        """

        # Initialize an empty list to store the decoded substrings
        decoded_string = []

        i = 0
        while i < len(str):

            # Find the index of the delimiter ":;"
            delimiter_index = str.find(":;")

            if delimiter_index != -1:
                # If the delimiter is found, append the substring from the current index to the delimiter index
                decoded_string.append(str[i:delimiter_index])

                # Remove the delimiter and the two characters following it from the string
                str = str[:delimiter_index] + str[delimiter_index + 2:]

                # Update the current index to the delimiter index
                i = delimiter_index
            else:
                # If the delimiter is not found, append the remaining substring and exit the loop
                decoded_string.append(str[i:])
                break

        return decoded_string


print(Solution().decode("we:;say:;yes"))
print(Solution().decode("w123:;sa123:;ye123:;123321"))
