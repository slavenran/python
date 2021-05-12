# book = dict()
# book["apple"] = 0.67
# book["milk"] = 1.3
# book["potato"] = 0.23

# print(book["potato"])



# phone_book = {}
# phone_book["jenny"] = 8675309
# phone_book["emergency"] = 911

# print(phone_book["jenny"])



voted = {}
def check_voter(name):
    if voted.get(name):
        print ("kick them out")
    else:
        voted[name] = True
        print("let them vote")

check_voter("marko")
check_voter("darko")
check_voter("marko")
check_voter("barko")