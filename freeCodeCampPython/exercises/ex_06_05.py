str = "X-DSPAM-Confidence: 0.8475 "

ws_pos = str.find(":")

num_extr = str[ws_pos+1:].strip()
# print(num_extr)

try:
    num = float(num_extr)
    print(num + 42.34)
except:
    print("Error")
