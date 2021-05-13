hours = float(input("Work hours: "))
rate = float(input("Pay rate: "))
# print(hours, rate)
pay = 0
if hours <= 40:
    pay = hours*rate
else:
    pay = 40*rate + (hours-40)*rate*1.5

print(f"Your pay is {pay} euros")