import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

closest = 10000

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)


# This condition ensures that if the new 't' value is the same as closest, then the positive number is returned
    if abs(t) == abs(closest):
        closest = abs(t)
    elif abs(t) <= abs(closest): 
        closest = t


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


if n == 0:
    print(0)
else:
    print(closest)

