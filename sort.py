# Python program for implementation of Selection

def selSort(A):
  for i in range(len(A)):
    
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
      if ord(A[min_idx].split("|")[2]) > ord(A[j].split("|")[2]):
        min_idx = j
        
    # Swap the found minimum element with
    # the first element		
    A[i], A[min_idx] = A[min_idx], A[i]

  # Driver code to test above
  '''
  print ("Sorted array")
  for i in range(len(A)):
    B = (A[i])
  '''
  
  return A