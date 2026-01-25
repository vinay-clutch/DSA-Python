# Palindrome Number

# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
# A palindrome number is a number which reads the same both left to right and right to left.
# Example 1
# Input: n = 121
# Output: true
# Explanation: When read from left to right : 121.
# When read from right to left : 121.
# Example 2
# Input: n = 123
# Output: false
# Explanation: When read from left to right : 123.
# When read from right to left : 321.


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