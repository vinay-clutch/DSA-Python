n = [1,2,3,6,10,1,3,5,5,9]
m = [10,111,1,9,5,3,67,2,3,1]

hash_list = [0]*11

for num in n:
  hash_list[num]+=1
for num in m:
  if num<1 or num>10:
    print(0)
  else:
    print(hash_list[num]) 


# for num in n:
#   count = 0
#   for x in m:
#     if num == x:
#       count+=1
#   print(count)         this is brute force method 


