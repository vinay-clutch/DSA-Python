def tolast(arr):
  result = []
  zero_count = 0
  for num in arr:
    if num != 0:
      result.append(num)
    else:
      zero_count += 1
  for a in range(zero_count):
    result.append(0)
  return result

print(tolast([1, 0, 2, 0, 0, 3]))
