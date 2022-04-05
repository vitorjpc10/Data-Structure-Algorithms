
from itertools import count


n = 5
finalArray = []

for i in range(0,n + 1):
     
     x = bin(i)
     y = x.count("1")
     finalArray.append(y)
     
     