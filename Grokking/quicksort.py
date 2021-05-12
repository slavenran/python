import timeit

start = timeit.default_timer()

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if pivot >= i]
    greater = [i for i in arr[1:] if pivot < i]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1, 5, 7, 20, 31, 11, 10, 91, 2, 3, 9, 4]))

stop = timeit.default_timer()
print("Time: ", stop - start)

##Picking random number from array
import random
from random import randrange

start = timeit.default_timer()

def quicksortRandom(arr):
    if len(arr) < 2:
        return arr
    randIndex = randrange(len(arr))
    pivot = arr.pop(randIndex)
    less = [i for i in arr if pivot >= i]
    greater = [i for i in arr if pivot < i]
    return quicksortRandom(less) + [pivot] + quicksortRandom(greater)

print(quicksortRandom([1, 5, 7, 20, 31, 11, 10, 91, 2, 3, 9, 4]))

stop = timeit.default_timer()
print("Time: ", stop - start)