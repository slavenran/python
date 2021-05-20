fname = input('Enter file: ')
if len(fname) < 1: fname = "clown.txt"
hand = open(fname)

di = {}
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1
# print(di)

## Concise way
list_tup = sorted([(v, k) for k, v in di.items()], reverse=True)
list_normalize = [(v, k) for k, v in list_tup]
print(list_normalize[:10])

## Procedural way
list_tup = []
for k, v in di.items():
    list_tup.append((v, k))
list_tup = sorted(list_tup, reverse=True)
list_normalize = []
for k, v in list_tup:
    list_normalize.append((v, k))
print(list_normalize[:10])