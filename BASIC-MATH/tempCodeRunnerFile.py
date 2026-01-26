def print_divisions(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
          divisors.append(i)
            #print(i)
        if i != n // i:
          divisors.append(n // i)  
    for d in sorted(divisors):
      print(d)

print_divisions(54)