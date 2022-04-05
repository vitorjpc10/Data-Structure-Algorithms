words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
     
charList = []
charList[:] = chars
goodTotal = 0


for j in range(0,len(words)): #every index at words list
     charTest = charList.copy()
     removedCount = 0
     
     for i in range(0, len(words[j])): #every char index at that word
     
          if words[j][i] in charTest:
               charTest.remove(words[j][i])
               removedCount += 1
          else:
               break
          
          if removedCount == len(words[j]):
               goodTotal += len(words[j])
               

print(goodTotal)