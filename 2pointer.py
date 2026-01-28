s = "anbcddcbna"

n = len(s)
left = 0
right = n - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)


'''


s = "anbcddbna"

n = s[::-1]

if n == s:
  print(True)
else:
  print(False)
  
  

'''


def is_palindrome(s, left, right):
    # Base case: pointers crossed or met
    if left >= right:
        return True

    # If characters do not match
    if s[left] != s[right]:
        return False

    # Recursive call (move inward)
    return is_palindrome(s, left + 1, right - 1)


# Driver code
s = "anbcddcbna"
result = is_palindrome(s, 0, len(s) - 1)
print(result)
