str_hours = input("Work hours: ")
str_rate = input("Pay rate: ")

# try:
#     hours = float(str_hours)
# except:
#     hours = -1

# try:
#     rate = float(str_rate)
# except:
#     rate = -1

try:
    hours = float(str_hours)
    rate = float(str_rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = 0
if hours <= 40:
    pay = hours*rate
else:
    pay = 40*rate + (hours-40)*rate*1.5

print(f"Your pay is {pay} euros")