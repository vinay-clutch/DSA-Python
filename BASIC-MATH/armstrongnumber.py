def checkamstrong(n):
  dup = n
  sum = 0
  while n>0:
    last = n%10
    sum += last**3
    n//=10
  if sum == dup:
    return True
  else:
    return False
  
print(checkamstrong(371))


"""
  
  def is_armstrong(n):
    return n == sum(int(d)**3 for d in str(n))

print(is_armstrong(371))

 """