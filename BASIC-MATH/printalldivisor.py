"""
def checkdivison(n):
  for i in range(1,n+1):
    if n % i == 0:
      return i
    else:
      return False
  
print(checkdivison(23))
"""

"""
def print_divisions(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
          divisors.append(i)
            #print(i)
            if i != n // i:   #This line is used to avoid printing #the same divisor twice when the number is a perfect square.
                #print(n // i)
                divisors.append(n // i)  
    for d in sorted(divisors):
      print(d)

print_divisions(54)

"""
def print_divisions(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
          divisors.append(i)
            #print(i)
        if i != n // i:
          divisors.append(n // i)  
    for d in sorted(divisors):
      print(d)

print_divisions(54)