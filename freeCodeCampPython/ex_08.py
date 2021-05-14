# file = open("mbox-short.txt")

# for line in file:
#     line = line.rstrip()
#     if not line.startswith("From "):
#         continue
#     print(line.split()[2])

han = open('mbox-short.txt')
for line in han:
    line = line.rstrip()
    # if line == "":
    #     continue
    wds = line.split()
    # if len(wds) < 3:
    #     continue
    if not wds or wds[0] != "From":         # if len(wds) < 3 or wds[0] != "From":
        continue
    print(wds[2])