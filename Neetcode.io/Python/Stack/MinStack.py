#! https://leetcode.com/problems/min-stack/
"""
155. Min Stack
Medium
13.1K
794
Companies
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack(object):
    def __init__(self):
        """
        Initializes a new instance of the MinStack class.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.stack = []
        self.min_value = None
        self.min_value_prev = []

    def push(self, val):
        """
        Pushes the specified value onto the stack.

        :param val: int - The value to be pushed onto the stack.
        :rtype: None

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.stack.append(val)

        if self.min_value is None:  # First push operation
            self.min_value = val
        else:
            new_min_value = min(val, self.min_value)

            if new_min_value == val:
                self.min_value_prev.append(self.min_value)
                self.min_value = val
            else:
                self.min_value = new_min_value

    def pop(self):
        """
        Removes the top element from the stack.

        :rtype: None

        Time complexity: O(1)
        Space complexity: O(1)
        """
        removed_value = self.stack.pop()

        if removed_value == self.min_value:
            if len(self.min_value_prev) != 0:
                self.min_value = self.min_value_prev.pop()
            else:
                self.min_value = None

    def top(self):
        """
        Returns the value of the top element in the stack without removing it.

        :rtype: int or None - The value of the top element, or None if the stack is empty.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        """
        Returns the minimum value in the stack.

        :rtype: int or None - The minimum value in the stack, or None if the stack is empty.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.min_value



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()