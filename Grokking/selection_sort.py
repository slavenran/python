def findSmallestIndex(arr):
    smallestNumber = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallestNumber:
            smallestNumber = arr[i]
            smallestIndex = i
    return smallestIndex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallestIndex(arr)
        newArr.append(arr.pop(smallestIndex))
    return newArr


print(selectionSort([6, 1, 3, 12, 1, 5, 32, 4]))