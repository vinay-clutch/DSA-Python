def counttarget(arr,t):
  left = 0
  right = len(arr)-1
  count = 0
  while left < right:
    sum = arr[left] + arr[right]
    if sum == t:
      count += 1
      left += 1
      right -= 1
    elif sum < t:
      left += 1
    else:
      right -= 1
  return count