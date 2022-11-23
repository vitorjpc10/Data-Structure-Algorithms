class Solution:
     def isAnagram(self, name1: str, name2: str) -> bool:
          """Solves Anagram using a stack, where it stacks a name, pops it, and compare with the other name

          Args:
              name1 (str): _description_
              name2 (str): _description_

          Returns:
              bool: _description_
          """          
          
         
          if len(name1) != len(name2):
               print("string lengths do not match")
               return False
          
         
          stack = []
          
          for char in name1:
               stack.append(char)
          
          print(stack)
          
          name1Destack=""
               
          while len(stack) !=0:
               name1Destack += stack.pop()
          
          return name1Destack == name2
     
     def isAnagram2(self, name1: str, name2: str) -> bool:
          """Solves an Anagram by sorting both arguments and compares if equal

          Args:
              name1 (str): _description_
              name2 (str): _description_

          Returns:
              bool: _description_
          """          
          
          return sorted(name1) == sorted(name2)
          

obj = Solution()
print(obj.isAnagram("catt", "tact"))
print(obj.isAnagram2("catt", "tact"))

