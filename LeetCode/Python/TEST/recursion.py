
#todo: Create a recursive method where sum of n is n plus all the previous non-negative numbers before


def sum(n):
     if n == 0:
          return 0
     else:
          return n + sum(n - 1)
          
print(sum(1))