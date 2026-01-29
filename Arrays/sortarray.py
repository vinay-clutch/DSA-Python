def issorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
    
  return True

print(issorted([2, 7, 6, 8]))


"""
Start from first element

Compare current element with next

If current > next → array is NOT sorted

If all comparisons pass → array IS sorted
"""