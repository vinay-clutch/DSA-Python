def secondlargest(arr):
  largest = arr[0]
  second_large = float('-inf')
  
  for i in range(len(arr)):
    if arr[i]>largest:
      second_large = largest
      largest = arr[i]
    elif arr[i]>second_large and arr[i] != largest:
      second_large = arr[i]
  return second_large      

print(secondlargest([3, 7, 1, 9, 2]))


""" 

LOGIC IN WORDS (MEMORIZE THIS)

Initialize:

largest = arr[0]

second = -∞ (or very small)

Loop through array:

If current > largest:

second = largest

largest = current

Else if current > second AND current != largest:

second = current




largest = 3, second = -1

see 7 → largest=7, second=3

see 1 → ignore

see 9 → largest=9, second=7

see 2 → ignore

✅ Answer = 7
"""