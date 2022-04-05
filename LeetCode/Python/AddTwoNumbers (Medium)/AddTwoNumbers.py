class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#?I wanted to add a comment here to see if it would be able to upload a change to github.com
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
     #l1 = [2,4,3]
     #l2 = [5,6,4]
     
     revL1 = l1[::-1]
     revL2 = l2[::-1]

     num1 = ''.join(str(i) for i in revL1)
     num2 = ''.join(str(i) for i in revL2)

     ans = str(int(num1) + int(num2))
     ans = ans[::-1]

     final  = []
     final[:0]= ans

     return final

obj1 = Solution()
print(obj1)

#! NOT SURE HOW TO USE A ListNode in this problem, was able to solve it using normal list though
     