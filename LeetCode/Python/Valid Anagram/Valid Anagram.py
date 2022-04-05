

def isAnagram(s: str, t: str) -> bool:
     final = True
     
     newString = s
     
     testString = []
     testString[:] = t
     
     for i in range(0,len(t)):
          
          if testString.count(s[i]) > 0:
              newString = newString.replace(s[i],'',1)
               
          else:
               final = False
               break
     
     return final, newString
               
     
     




print("is a anagram?: %b",isAnagram("rat","car"))