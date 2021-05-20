import socket

input_str = input("What address to crawl? ")

try:
    host_name = input_str.split('/')[2]
except:
    print("Address not formated correctly")
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host_name, 80))
    cmd = f'GET {input_str} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
except:
    print("Page not formated correctly or doesn't exist")
    quit()

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if count <= 3000:
        print(data.decode(),end='')
    count += len(data)

print("\nNumber of characters on this page is: ", count)
mysock.close()

# http://data.pr4e.org/romeo-full.txt