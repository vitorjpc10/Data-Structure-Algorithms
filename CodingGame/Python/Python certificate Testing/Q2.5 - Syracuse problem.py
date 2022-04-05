#2022-03-22-08-52-37.png


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 5
result = str(n)  + " "
calc = int(n)


while calc != 1:
    
    if calc % 2 == 0: # if even
        calc = int(calc / 2)
        result += str(calc) + " "
    else: # if odd
      
        calc = int((calc * 3) + 1) 
        result += str(calc) + " "
        
        
        
result = result[:-1]

print(result)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


