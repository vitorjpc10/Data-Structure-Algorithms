
def containsDuplicate(nums: list[int]) -> bool:
    return (len(set(nums)) != len(nums))  

list = [1,2,3,4,5,6,6]
print(containsDuplicate(list))





