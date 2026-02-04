# def twosum(arr,target):
#   seen = {}
  
#   for i in range(len(arr)):
#     need = target - arr[i]
#     if need in seen:
#       return[seen[need],i]
#     seen[arr[i]] = i
  

def towsum(arr,target):
  left = 0
  right = len(arr)-1
  while left < right:
    s = arr[left] + arr[right]
    if s == target:
      return [left,right]
    elif s<target:
      left += 1
    else:
      right -= 1
  