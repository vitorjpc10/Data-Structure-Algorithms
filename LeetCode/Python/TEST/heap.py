#! https://www.tutorialspoint.com/python_data_structure/python_heaps.htm

#todo: Messing with heaps in Python

import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print("heapify example output: " + str(H))
#! Notice the resulting heap the smallest element gets pushed to the index position 0


#! Add element
heapq.heappush(H,8)
print ("heappush example output: ", str(H))

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)