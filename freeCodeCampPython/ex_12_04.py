import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

input_str = input("What address to crawl? ")

try:
    file = urllib.request.urlopen(input_str).read()
except:
    print("Page doesn't exist or address not formatted propertly")
    quit()

output = BeautifulSoup(file, 'html.parser')

# print(output.decode())       # docodes the whole page for printing

tags = output('p')

print(f'{len(tags)}')

# http://data.pr4e.org/romeo-full.txt