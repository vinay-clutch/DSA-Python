def secondndlarge(arr):
  max = 0 
  min = 0
  for i in range(len(arr)):
    if arr[i]>max:
      min = max
      max = arr[i]
    elif arr[i]>min and arr[i]!=max:
      min = arr[i]
  return min

print(secondndlarge([3, 7, 1, 9, 2]))