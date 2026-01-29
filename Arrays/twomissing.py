def twoMissingNumbers(arr, n):
    s = set(arr)
    missing = []

    for num in range(1, n + 1):
        if num not in s:
            missing.append(num)

    return missing

print(twoMissingNumbers([2, 3, 6, 7], 7))
