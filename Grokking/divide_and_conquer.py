def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([2, 4, 6]))

##Recursive (mine)
def sumRec(arr):
    if len(arr) == 0: return 0
    return arr.pop(0) + sumRec(arr)

print(sumRec([2, 4, 6]))

##Recursive (textbook)
def sumRecAnswer(arr):
    if arr == []: return 0
    return arr[0] + sumRecAnswer(arr[1:])

print(sumRecAnswer([2, 4, 6]))

##No. of items recursive (mine)
def countNo(arr):
    if arr:
        arr.pop(0)
        return 1 + countNo(arr)
    return 0

print(countNo([1,2,3,4,8,9,67]))

##No. of items recursive (textbook answer)
def countNoAnswer(arr):
    if arr == []:
        return 0
    return 1 + countNoAnswer(arr[1:]) #arr[1:] vraca sve nakon prvog elementa (arr[1:5] vraca 4 elementa od prvog do petog)

print(countNoAnswer([1,2,3,4,8,9,67]))

##Max
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    maxNo = max(list[1:])
    return list[0] if list[0] > maxNo else maxNo
        ##moj take na ovo
        # if list[0] > list[1]:
        #     list[1] = list[0]
        # return max(list[1:])

print(max([1, 4, 6, 2]))

