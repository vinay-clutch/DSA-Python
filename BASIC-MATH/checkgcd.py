def checkgcd(a , b):
  while a != 0 and b != 0:
    if a>b:
      a %= b
    else:
      b %= a
  if a == 0:
    print(b)
  else:
    print(a)
    
checkgcd(20,40)


# this is eucliden alg based approch
"""
def checkgcd(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)

checkgcd(20, 40)


                                                                  a, b = b, a % b

                                                                  This does two assignments at once:

                                                                  New a becomes old b

                                                                  New b becomes a % b (remainder)
                                                                  a % b = 20 % 40 = 20
                                                                  a = 40
                                                                  b = 20                
                                                                  
  """
