#Stack

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

greet("maggie")

########################################################

#Recursion

i = 3

def countdown(i):
    print(i)
    if i <= 0:
        return
    countdown(i-1)

countdown(i)

########################################################

#Factoriels

##recursive
def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

##non-recursive
def factorial2(x):
    res = 1
    if x <= 1:
        return res
    else:
        num = x
        while num > 1:
            res *= num * (num - 1)
            num -= 2
        return res

print(factorial2(5))

##tail-recursion
def factorialTail(x, accumulator=1):
    if x <= 1:
        return accumulator
    else:
        return factorialTail(x-1, accumulator*x)

print(factorialTail(5))

##tail-recursion without recursion (probably the best solution)
def trisum(x, accumulator=1):
    while True:
        if x <= 1:
            return accumulator
        x, accumulator = x - 1, accumulator * x

print(trisum(5))