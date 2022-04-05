def findSimilar(a, b):
     
     for i in range(0,len(a)):
          
          test = a[i] in b

          if test == True:
               continue
          else: 
               return len(b)
               
     
     return len(a)
    
    


print(findSimilar("112", "121"))
