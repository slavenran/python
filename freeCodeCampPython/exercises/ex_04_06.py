def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    return 40 * rate + (hours - 40) * rate * 1.5

str_hours = input("Your work hours: ")
str_rate = input("Your pay rate: ")

try:
    hours = float(str_hours)
    rate = float(str_rate)
except:
    print("You must enter numeric values")
    quit()

print(f"Your pay will be {computepay(hours, rate)} euros.")