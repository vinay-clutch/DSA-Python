def missingnumber(arr,n):
  total = n * (n+1)//2
  arr_sum = 0
  
  for i in arr:
    arr_sum += i
  return total - arr_sum

print(missingnumber([1, 3, 4, 5],5))
  