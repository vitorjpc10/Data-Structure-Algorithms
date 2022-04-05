def findSmallestDivisor(s, t):
    
     
    
     sList = []
     sList[:] = s
     
     counter = 1
     test = ''.join(sList[0:counter])
     
     for i in range(0,len(sList)):
          
          if test * 2 in s:
               return len(test)
          else:
               counter += 1
               test = ''.join(sList[0:counter])
    
     if s == t: return len(s)
    
     return -1
    
         
    
    
    

print(findSmallestDivisor("lrbb","lrbb"))