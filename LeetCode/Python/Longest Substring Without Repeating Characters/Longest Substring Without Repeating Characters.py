from xml.etree.ElementPath import find


def lengthOfLongestSubstring(s: str) -> int:
     totalLength = 0
     largestLength = 0
     uniqueList = []
     
        
     for i in range(0,len(s)):
          chatAt = s[i]
          
          if i == 0:
               uniqueList.append(s[i])
               totalLength += 1 
          
          elif s[i] in uniqueList:
               
               
               if totalLength > largestLength:
                    largestLength = totalLength
                    
               uniqueList = []
               totalLength = 0
               
               lastInstance = s[:i].rfind(s[i])
               correctedInstance = s[lastInstance+1:i+1] 
               
               uniqueList[:0] = correctedInstance
               totalLength = len(uniqueList)
               
                    
          else:
               uniqueList.append(s[i])
               totalLength += 1
                 
     if totalLength > largestLength:
          largestLength = totalLength    
                   
     return largestLength
     


print("Total length is: " + str(lengthOfLongestSubstring("abcabcbb")))
      
#todo: Good Job you did it!


