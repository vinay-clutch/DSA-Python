def func(num):
    if num == 0 or num == 1:
        return num
    return func(num - 1) + func(num - 2)


"""

   
func(4)
 ├─ func(3)
 │   ├─ func(2)
 │   │   ├─ func(1) → 1
 │   │   └─ func(0) → 0
 │   └─ func(1) → 1
 └─ func(2)
     ├─ func(1) → 1
     └─ func(0) → 0

"""