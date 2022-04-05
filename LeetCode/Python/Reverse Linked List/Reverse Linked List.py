class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        
        # store data
        self.data = data
        
        # store reference (next item)
        self.next = None
        return
    
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dictionary = {}
        while head:
            if head in dictionary: 
                return True
            else: 
                dictionary[head]= True
            head = head.next
        return False




obj = Solution()
obj1 = ListNode([3,2,0,-4])
print(obj.hasCycle(obj1))
   