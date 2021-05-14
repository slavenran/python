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

## Functions and loops
def loopFun():
    i = 1
    while True:
        if i == 3:
            break
        i += 1
    for j in [3, 2, 5, 2]:      ## for is prefered whenever is possible to use it
        print(j)

## == and is
smallest = None
if smallest is None:        ## None is stronger than == because it also compares types, used mostly on boolean and None types
    print("Empty")

## Strings
for n in "banana":
    print(n)        ## prints each letter

len("banana")       ## returns length of the array (string is an array of characters)

## Slicing
s = "Monty Python"
print(s[0:4])
print(s[6:20])      ## iako je 20 out of bounds, ne vraca traceback vec se zaustavlja na poslednjem karakteru
print(s[:2])        ## prvi i drugi argument se mogu izostaviti ako hocemo od pocetka da krenemo ili od kraja, respectively
print(s[8:])

## in as logical operator
'n' in 'fruit'      # logical operation that return boolean value
if "na"  in  "banana":
    print("its in the banan!")

## String comparison
if word == "banana":
    print("A banana")
elif word > "banana":
    print("Comes after banana")
elif word < "banana":
    print("Comes before banana")
else:
    print("Empty")

## String library
greet = "HELLO"
low = greet.lower()     # gives back same string but in all lowercase
big = low.upper()       # -||-  but in all uppercase

dir(greet)      # u ovom slucaju vracaa sve metode koje mogu da se pozovu stringom

test_str = "super banana"
pos = test_str.find("na")       # returns the starting position of this substring
pos = test_str.find("na", 5)    # returns first position of first na after the position 5

greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")     # finds and replaces all instances of Bob with Jane

greet = "   Hello Bob   "       # stripping whitespace from left and right    
greet.lstrip()
greet.rstrip()
greet.strip()

line = "Please have a nice day"
line.startswith("Please")       # true
line.startswith("p")            # false (lowercase)

## Reading files
file = open("mbox.txt", "r")  # open(filename, mode), r for reading and w for writing
for line in file:             # iterating through the file lines and prints them out
    print(line)

file.read()                   # returns file as a single string (not good for big files - might overload)

file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

## Data structures - Lists
list_test = [2, 3, 6]
print([1, 2, 3])
print(["red", "yellow", "green"])
print(["red", 32, 43.32])
print([1, [4, 5], 6])
print([])

len(list_test)            # prints list length
range(list_test)          # used to construct loops when we need to know the index number!

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print(friend, friend)
for i in range(len(friends)):
    print(friends[i], i)

x = [1, 2, 3] + [4, 5, 6]       # list concatinating
y = x[1:6]                      # list slicing

x = list()                      # deklaracija prazne liste, moze i x = []
x.append('book')
x.append('cookie')
'cookie' in x                   # boolean

x.sort()                        # list sorting

max(y)
min(y)
sum(y)

numbers = list()                # uses more memory but not much
while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        num = float(num_str)
    except:
        print("You must enter a number")
        continue
    numbers.append(num)

print(sum(numbers), len(numbers), sum(numbers)/len(numbers))

# String and lists
test_str = "Marko je mali pacov"
word_list = test_str.split()        # makes a list of words

test_str = "Marko;je;mali;pacov"
word_list = test_str.split(";")     # split can take an argument as a spliting parameter (delimiter)

file = open("mbox-short.txt")       # example file split
for line in file:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[2])

