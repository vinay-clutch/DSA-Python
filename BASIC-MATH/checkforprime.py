def checkprime(n):
  count = 0
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      count += 1
  if count == 2:
    print("prime")
  else:
    print("not a prime number")
    
    
checkprime(11)



"""
def checkprime(n):
    if n <= 1:
        print("not a prime number")
        return

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("not a prime number")
            return

    print("prime")
  
  """