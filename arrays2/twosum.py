def twosum(arr,target):
  seen = {}
  
  for i in range(len(arr)):
    need = target - arr[i]
    if need in seen:
      return[seen[need],i]
    seen[arr[i]] = i
  