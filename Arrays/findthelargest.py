def largestnum(arr):
  maxarr = arr[0]
  for i in range(len(arr)):
    if arr[i]>maxarr:
      maxarr = arr[i]
      
  return maxarr

print(largestnum([10, 4, 6, 2, 9]))

"""
Step-by-step logic (memorize this pattern):

Assume first element is largest

Compare it with others

Update if you find bigger

"""

def largestnum(arr):
  max_no = arr[0]
  for i in range(len(arr)):
    if arr[i]>max_no:
      max_no = arr[i]
  return max_no

print(largestnum([3,7,1,9,2]))