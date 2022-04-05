from operator import index


def groupDivision(levels, maxSpread):
    
    #!sorting the levels list by
     levels = sorted(levels)
     totalGroups = 00
     indexPlus = 1
     index = 0
    
    
     for i in range(len(levels)):
         if levels[index + indexPlus] <= maxSpread + levels[index]:
               totalGroups += 1
               indexPlus += 1
         else:
              index += 1
              indexPlus = 1

     return totalGroups
    
    
    



print(groupDivision([4,1,2,5,3], 0))    