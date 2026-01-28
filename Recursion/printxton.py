def times(x,n):
  if n==0:
    return
  print(x)
  return times(x,n-1)

times(15,5)