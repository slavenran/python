import re
file = open("mbox-short.txt")

nums = []
for line in file:
    line = line.rstrip()
    num = re.findall('New Revision: ([0-9]+)', line)
    if len(num) > 0:
        nums.append(int(num[0]))
print(int(sum(nums)/len(nums)))