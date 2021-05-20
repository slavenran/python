# filename = input("Enter a file name: ")

# try:
#     file_string = open(filename)
# except:
#     print("That file doesn't exist")
#     quit()

# print(file_string.read().upper())


filename = input("Enter a file name: ")

try:
    file = open(filename)
except:
    print("That file doesn't exist")
    quit()

i = 0
for line in file:
    line_clean = line.rstrip().upper()
    print(line_clean)
    i += 1
    if i == 10:
        break
