
def rotate(arr,d):
  n = len(arr)
  d =  d % n
  for _ in range(d):
    first = arr[0]
  
    for i in range(1,n):
      arr[i-1]= arr[i]
    arr[-1] = first
  
  
  return arr

print(rotate([3, 4, 5, 1, 2],2))