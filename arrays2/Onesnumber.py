def check1number(arr):
  freq = {}
  for num in arr:
    if num in freq:
      freq[num] += 1
    else:
      freq[num] = 1
      
  for num in freq:
    if freq[num] == 1:
      return num
print(check1number([2, 2, 1, 4, 4]))  