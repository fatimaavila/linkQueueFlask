# Python program for implementation of Selection
# Sort
import __main__

def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append('<a href="'+node.data.split("|")[0]+'" target="_blank">'+node.data.split("|")[1]+node.data.split("|")[2]+'</a>')
      __main__.sorteado.append(node.data)
      node = node.next
    nodes.append("")
    return "<br>".join(nodes)

def selSort(A):
  for i in range(len(A)):
    
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
      if ord(A[min_idx].split("|")[1]) > ord(A[j].split("|")[1]):
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