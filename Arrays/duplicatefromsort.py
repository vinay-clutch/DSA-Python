def removedup(arr):
  result = [arr[0]]   # keep first element

  for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
          result.append(arr[i])
  return result

print(removedup([1, 1, 2, 2, 3, 3]
))