arr = [12,23,0,34,0,44,0]

# temp = []

# for i in arr:
#   if i != 0:
#     temp.append(i)
# zero = len(arr)-len(temp)
# temp.extend([0]*zero)
# print(temp)


# 2nd approach
'''


def zerotoend(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr
'''
'''
def pushZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

'''

