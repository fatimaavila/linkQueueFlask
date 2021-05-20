# Python program for implementation of Selection
# Sort
import sys
A = ["o", "b", "h", "a", "0"]

# Traverse through all array elements
for i in range(len(A)):
	
	# Find the minimum element in remaining
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if ord(A[min_idx]) > ord(A[j]):
			min_idx = j
			
	# Swap the found minimum element with
	# the first element		
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print(A[i]),