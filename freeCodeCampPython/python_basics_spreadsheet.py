## Operations
a = 4 + 13      # Addition
b = 31 - 12     # Subtraction
c = a * b       # Multiplication
d = a / b       # Division (returns float)
e = a // b      # Division (returns floor int)
f = a % b       # Remainder of division

## Types and conversions
num = 4
floatNum = float(num)       # Converts from int to float (can go other way around)
word = "2323"
wordNum = int(word)         # Converts from string to number (float, int)
print(type(wordNum))        # Checks the type of the variable or constant

## User input
nam = input("Who are you? ")
print("Welcome", nam)

inp = input("Europe floor? ")
usf = int(inp) + 1
print("US floor:", usf)

## Comparison
a < b       # Less than (also >)
a <= b      # Less or equal to (also >=)
a == b      # Equal to
a != b      # Not equal to

## Multi-way
x = 0
if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")
print("All done")

## Try/except
rawstr = input("Enter a number:")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print("Not a number")

try:        # try with a quit() function
    ival = int(rawstr)
except:
    print("Error, please enter a number")
    quit()