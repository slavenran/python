def fibonacci_closest_number(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    list = [0, 1, 1]
    i = 2
    while True:
        num = list[i] + list[i-1]
        if num > x: break
        list.append(num)
        i += 1
    return list

print(fibonacci_closest_number(100))

## This is a recursive function, don't use it, really slow
# def fibonacci_number_at(x):
#     if x == 0:
#         return 0
#     if x == 1:
#         return 1
#     return fibonacci_number_at(x-2) + fibonacci_number_at(x-1)

# print(fibonacci_number_at(15))

##Tail recursion, sonic the hedgehog fast
def fibonacci_number_at(x):
    if x < 1:
        return 'Invalid number'
    a, c = 0
    b = 1
    for i in range(x-1):
        c = a + b
        a, b = b, c
    return a

def fibonacci_number_at_print(x):
    if x < 1:
        return 'Invalid number'
    a, c = 0
    b = 1
    for i in range(x):
        print(a)
        c = a + b
        a, b = b, c

num_str = input('Enter a number: ')
try:
    num = int(num_str)
except:
    print('Numbers only')
    quit()
print(fibonacci_number_at(num))
# fibonacci_number_at_print(num)