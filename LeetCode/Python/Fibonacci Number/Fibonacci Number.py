def climb(n):
     if n==1: #only one step option is availble
                 return 1
     if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
                 return 2
             
     n0 = 1
     n1= 2
             
     for i in range(3, n+1):
                  np = n0 + n1
                  
                  n0 = n1
                  n1 = np
                  
     return np
          
          
print(climb(4))