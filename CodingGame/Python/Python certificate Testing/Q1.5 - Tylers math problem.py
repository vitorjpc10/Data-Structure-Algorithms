#2022-03-22-08-46-18.png

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

calc = input()

strWOPlus = calc.replace('+',"")
calcArray = []
total = ""


for char in strWOPlus:
    calcArray.append(char)


calcArray.sort()


index = 0

for i in calcArray:
    
    if index == len(calcArray) - 1:
        total += i
    else:
        total += i + '+'

    index += 1

   

print(total)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)