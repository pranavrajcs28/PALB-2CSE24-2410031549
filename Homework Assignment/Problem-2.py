def getMinMax(arr):
    minVal = maxVal = arr[0]
    for x in arr[1:]:
        if x < minVal:
            minVal = x
        if x > maxVal:
            maxVal = x
    return minVal, maxVal

arr = [1,4,3,5,8,6]
print(getMinMax(arr))