s = "anbcddbna"

n = s[::-1]

if n == s:
  print(True)
else:
  print(False)
  
  
n = len(s)
left = 0
right = n-1
while left<right:
  if s[left]!=s[right]:
    print(False)
  left +=1
  right-=1
else: 
  print("gooo")