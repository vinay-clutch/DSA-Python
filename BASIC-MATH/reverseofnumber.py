# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
# Example 1

# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.

# Example 2

# Input: n = 123
# Output: 321
# Explanation: Reverse of 123 is 321.

"""
def reverseofnumber(n):
  rev = 0
  while(n > 0):
    lastdigit = n%10             # get last digit
    rev = (rev * 10) + lastdigit
    n = n//10 # remove last digit
  return rev

print(reverseofnumber(int(7789)))
"""



"""
  def reverseNumber(self, n):
        return int(str(n)[::-1])
"""