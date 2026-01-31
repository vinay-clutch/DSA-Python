def checkroarr(arr):
  min = arr[0]
  min_index = 0
  for i in range(1,len(arr)):
    if arr[i]< min:
      min = arr[i]
      min_index = i
  return min , min_index

print(checkroarr([4, 5, 6, 7, 1, 2, 3]))