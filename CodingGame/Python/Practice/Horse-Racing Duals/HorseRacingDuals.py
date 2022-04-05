from operator import index
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

strDiff = math.inf

"""n = int(input())

array = [n]

for i in range(n):
    pi = int(input())
    array.append(pi)

"""
array = [10,5,15,17,3,8,11,28,6,55,7]
array.sort()

for i in range(0, len(array)):
    x = i

    if i == 0:
        pass
    elif array[i] - array[i-1] < strDiff and array[i] > array[i-1]:
        strDiff = array[i] - array[i-1]
    elif array[i-1] - array[i] < strDiff and array[i-1] > array[i]:
        strDiff = array[i-1] - array[i]
        
print(strDiff)


    
    
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

