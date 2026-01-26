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
