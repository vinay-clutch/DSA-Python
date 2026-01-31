def maximum(arr):
  n = len(arr)
  count = 0
  max_count = 0
  for i in range(n):
    if arr[i]==1:
      count += 1
      max_count = max(max_count,count)
    else:
      count = 0

  return max_count

print(maximum([1, 0, 0, 0, 0,1]))   


"""  this is correct code 
def maximum(arr):
    count = 0
    max_count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count



Maximum Consecutive Ones means:

Count 1s continuously

Reset when 0 appears

Keep track of the maximum count at any time

So we need TWO variables, not one.

✅ CORRECT THINKING (PLAIN ENGLISH)

You need:

count → current consecutive 1s

max_count → maximum consecutive 1s seen so far

Logic:

If element is 1 → increase count

If element is 0 → reset count to 0

After every step → update max_count
"""