def pushZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
            
print(pushZerostoEnd([12,23,0,34,0,44,0]))