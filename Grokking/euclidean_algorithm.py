def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    q = a//b
    r = a-b*q
    return gcd(b, r)

print(gcd(270, 192))

##No recursion tail recursion
def gcd2(a, b):
    while True:  
        if a == 0:
            return b
        if b == 0:
            return a
        q = a//b
        r = a-b*q
        a, b = b, r

print(gcd2(270, 192))