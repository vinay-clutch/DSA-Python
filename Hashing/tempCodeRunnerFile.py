words = "aabcc"
# n = len(words)
# print(n)
hash_list=[0]*26
  
for ch in words:
  index = ord(ch)-97
  hash_list[index]+=1
for ch in words:
  index = ord(ch)-97
  print(ch ,":" ,hash_list[index])