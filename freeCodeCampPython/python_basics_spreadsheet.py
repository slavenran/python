# ⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨
# ⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀
# ⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀
# ⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀
# ⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑
# ⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨
# ⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪
# ⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽
# ⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹
# ⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔
# ⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏
# ⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨
# ⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐
# ⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰
# ⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣
# ⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪
# ⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻
# ⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩
# ⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞
# ⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎
#              Welcome



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

## String and lists
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

## Dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

purse['candy'] = purse['candy'] + 1

purse2 = {}

print(purse['phone'])   # returns an error because phone is not in the purse
'phone' in purse        # checking if value is present in dictionary (below is the .get() metod showcase for this)

counts = {}                 # counting the number of names into dict (better way below)
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

x = purse.get('phone', 0)   # the way of checking if a key is present in a dictionary (0 is a value that returns if a key is not present)

counts = {}                 # best way of dealing with dictionaries
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

text_str = input("Your text: ")
words_txt = text_str.split()
words = {}
for word in words_txt:
    words[word] = words.get(word, 0) + 1
print(words)

for a, b in purse.items():  # python-only feature to iterate both values at the same time
    print(a, b)

## Tuples
x = ('Glenn', 'Sally', 'Joseph')        # similar to lists, only difference is tuples are immutable
x, y = 4, 'fred'                        # tuple assignment (python exclusive feature)

(0, 1, 2) < (5, 1, 2)                   # returns true without checking second and third comparison

c = {'a':10, 'b':1, 'c':22}             # sorting dict by value instead of key
tmp = []
for k, v in c.items():
    tmp.append((v, k))                  # key point (list can't take 2 elements as an element but it can take a tuple of more elements)
print(tmp)
tmp = sorted(tmp, reverse=True)
for val, key in tmp:                    # brings back order of key and value while it stays sorted
    print(key, val)

c = {'a':10, 'b':1, 'c':22}
print(sorted([(v, k)  for k, v in c.items()], reverse=True))  # short version of dict to list conversion

## Regular expressions
import re
re.search()
re.findall()
x = "My 2 favourite memebers are 19 and 42"
y = re.findall('[0-9]+', x)
print(y)

hand = open('mbox-short.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print(max(numlist))

icecream = "That icecream costs $10.54, my guy that's a lot"

find_cost = re.findall('\$[0-9.]+', icecream)
print(find_cost)

## Networking
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:                                                         # mini-browser
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

# urllib
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
arr = sorted([(v, k) for k, v in counts.items()], reverse=True)
print([(v, k) for k, v in arr])

## Web Scraping
from bs4 import BeautifulSoup
url = input('Enter - ')                         # scraping external links from web page
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
