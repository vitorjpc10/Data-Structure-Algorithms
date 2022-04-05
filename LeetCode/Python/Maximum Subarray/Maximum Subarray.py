def maxSubArray (nums: list[int]) -> int:
     
     m=nums #copy nums array into a new array 'm'
        
     for i in range(1,len(nums)):
            m[i]=max(m[i],m[i-1]+nums[i]) #update the element in M at the index of the current element scanned in nums 
            
     return max(nums)



print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))