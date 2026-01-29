"""
arr = [5, 3, 7, 1, 9]
target = 7

----------
HOW TO THINK (STEP BY STEP)

Start from first element

Compare each element with target

If match → return index

If loop ends → return -1
----------------------

i = 0 → 5 == 7 ❌

i = 1 → 3 == 7 ❌

i = 2 → 7 == 7 ✅ → return 2
"""
def checkindex(arr,target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1
    
print(checkindex([1, 2, 3, 4], 4))
  