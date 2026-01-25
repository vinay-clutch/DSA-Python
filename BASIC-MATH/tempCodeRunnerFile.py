def checkpalindrome(n):
  dup = n
  rev = 0
  while n>0:
    lastdigit = n%10  #this get last digit
    rev = rev*10 + lastdigit
    n = n//10  #this remove the last digit
  if rev == dup:
    return True
  else:
    return False
  
print(checkpalindrome(1221))