import urllib.request, urllib.parse, urllib.error

input_str = input("What address to crawl? ")

try:
    file = urllib.request.urlopen(input_str)
except:
    print("Page doesn't exist or address not formatted propertly")

output = file.read().decode()

print(f'{output[:3000]}\n\nNumber of character in this document: {len(output)}')

# http://data.pr4e.org/romeo-full.txt