
"""

def checkgcd(a,b):
  if b == 0:
    return a
  return checkgcd(b,a%b)
  
  
checkgcd(12,23)



"""

def checkgcd(a,b):
  if b == 0:
    return a
  return checkgcd(b,a%b)
  
  
print(checkgcd(12,23))