def fizzBuzz(n):
    
   for i in range(1,n+1): 
    
     if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
     elif i % 3 == 0 and i % 5 != 0: print("Fizz")
     elif i % 5 == 0 and i % 3 != 0: print("Buzz")
     else: print(i)
     
def simpleArraySum(ar):
     
     totalSum = 00
     
     for i in range(0,len(ar)):
          totalSum += ar[i]
     
     return totalSum


def compareTriplets(a, b):
     aSum = 00
     bSum = 00
     
     for i in range(0,len(a)):
          if a[i] == b[i]: continue
          
          if a[i] > b[i]: aSum += 1
          else: bSum += 1
     
     return aSum, bSum

def aVeryBigSum(ar):
     
     totalSum = 00
     
     for i in range(0,len(ar)):
          totalSum += ar[i]
     
     return totalSum

def diagonalDifference(arr):
     
     diag1 = 00
     diag2 = 0

     diag2Counter = len(arr) - 1
     
     for i in range(0,len(arr)):
          diag1 += arr[i][i]
          
     for i in range(0,len(arr)):
          diag2 += arr[i][diag2Counter]
          diag2Counter += -1
     
     return abs(diag1 - diag2)
     
     
#fizzBuzz(15)
print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))

          
     