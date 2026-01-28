# # character hashing

# s="azyxyyzaaa"
# q = ["a","d","y","u"]

# hash_list=[0]*26

# for ch in s:
#   # ascii_value =ord(ch)
#   index = ord(ch) - 97
#   # index = ascii_value-97
#   hash_list[index]+= 1
# for ch in q:
#   index = ord(ch) - 97
#   # ascii_value = ord(ch)
#   # index = ascii_value-97
#   print(hash_list[index])
  
words = "aabcc"
# n = len(words)
# print(n)
hash_list=[0]*26
  
for ch in words:
  index = ord(ch)-97
  hash_list[index]+=1
for ch in set(words):
  index = ord(ch)-97
  print(ch ,":" ,hash_list[index])