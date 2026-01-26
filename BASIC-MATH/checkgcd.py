def checkgcd(a , b):
  while a>b and b>a:
    if a>b:
      a %= b
    else:
      b %= a
  if a == 0:
    print(b)
  else:
    print(a)
    
checkgcd(20,40)