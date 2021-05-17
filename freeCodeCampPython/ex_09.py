fname = input('Enter file: ')
if len(fname) < 1: fname = "clown.txt"
hand = open(fname)

di = {}
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1
print(di)

largest = -1
big_word = None
for word, count in di.items():
    if count > largest:
        largest = count
        big_word = word
print(big_word, largest)