import sys
import math
import binascii

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()


#TODO: This is to get message length and set you transformation from input into binary
messageLength = len(message)
binaryRep = ""

#TODO: At each char of the message input, 1.transform in Hex, 2.From hex change into 7bit representation, 
#TODO: 3. append binary conversion into binary representation string
for i in message:
     messageHex = ord(i)
     binary_string = format(messageHex, '0>7b')
     binaryRep += binary_string
   
tempBinaryRep = ""
count = 1

iValue = 0

# TODO: now use string slicing to create the final binary representation based on the 1s and 0s values


for i in range(0,len(binaryRep)):
          #! go through string and check for a change from 0 to 1, or 1 to 0
     iValue = binaryRep[i]
     if i == 0:
               
          if int(binaryRep[i]) == 1: #if digit = 0, then 00
               tempBinaryRep += "0 " #if digit = 1, then 0
               pass 
          elif int(binaryRep[i]) == 0:
               tempBinaryRep += "00 "
               pass  
          
                  
     elif binaryRep[i] == binaryRep[i-1]:
          count += 1
     elif binaryRep[i] != binaryRep[i-1]:
          tempBinaryRep += (count * "0") + " "
               
          if int(binaryRep[i]) == 0:
               tempBinaryRep += "00 "
          else:
               tempBinaryRep += "0 "
                    
          count = 1
               
tempBinaryRep += (count * "0")
  
             
     #! specify 0 for 1 and 00 for 0, keep track of how many digits it repeats
     #! append initial part1 and part 2 and add to finalBinaryRep string



#for i in range(messageLength):

print(tempBinaryRep)   




# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


