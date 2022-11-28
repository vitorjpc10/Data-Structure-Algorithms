# def twoSum(nums: list[int], target: int) -> list[int]:
#      seen = {}
     
#      for index, value in enumerate(nums):
#           remaining = target - nums[index]
          
#           if remaining in seen:
#                return [index, seen[remaining]]
          
#           seen[value] = index   
          
# list= [3,5,7,0]
# target = 10


def twoSum2(nums: list[int], target: int) -> list[int]:

     pastValues = {}
     
     for i,value in enumerate(nums):
          remaining = target - nums[i]
          
          if remaining in pastValues:
               return [pastValues[remaining], i]
          
          pastValues[value] = i


list= [3,5,7,0]
target = 10

print(twoSum2(list, target))

#!Playing around with enums
# string = "Banana"

# for i in range(len(string)):
#      print(string[i])
     
# string = "Potato"

# print("\n")

# for i, char in enumerate(string):
#      print(char)