class Solution:
    
    def __init__(self):
        self.t = dict() # Used for Memoization
        return
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        # !Base Case: Check if the current target is achievable by
        # !the current number of dice given f faces
        if d*f < target:
            return 0
        
        # Base Case: Check when dice is equal to 1, can the
        # target be achieved by the given f faces
        if d==1:
            if 0 < target <= f:
                return 1
            else:
                return 0
        
        # Make key
        key = (d, target)
        
        # For the current no. of dices, check all possible ways
        # the to achieve target, only if the key doesn't exist
        if key not in self.t:
            
            # Init
            count = 0
            
            # For each possible value of face, subtract the face
            # value from the target and then call again the same
            # function with one less dice.
            for i in range(1,f+1):
                count += self.numRollsToTarget(d-1, f, target-i)
            
            # Memoization
            self.t[key] = count 
            
        return self.t[key] % ((10**9)+7) # return the current value
   
obj = Solution()
print(obj.numRollsToTarget(2,6,7))
