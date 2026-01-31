def checkleftar(arr):
  count = 0
  n = len(arr)
  for i in range(n):
    if arr[i]> arr[(i+1)%n]:
      count += 1
      
  return count <=1
print(checkleftar([3, 4, 5, 1, 2]))
print(checkleftar([2, 1, 3, 4]))

""" 
In a normally sorted array, numbers only increase.

In a left-rotated sorted array:

The increase breaks only once

That break happens where rotation occurred


(i + 1) % n lets us compare last element with first

This is necessary to detect rotation correctly



If this happens:

0 times → already sorted → OK

1 time → rotated sorted → OK

More than 1 time → NOT rotated sorted
"""