class Category():
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.amount = 0
        self.spent = 0

    def check_funds(self, amount):
        if amount > self.amount:
            return False
        return True

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.amount += amount

    def withdraw(self, amount, description=''):
        self.ledger.append({"amount": -amount, "description": description})
        if self.check_funds(amount):
            self.amount -= amount
            self.spent += amount
            return True
        return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.category_name}')
        category.deposit(amount, f'Transfer from {self.category_name}')
        return True

    def __str__(self):
        stars_no = 30 - len(self.category_name)
        extra = 0
        if stars_no % 2 != 0: extra = 1
        stars_no //= 2
        result = '*'*stars_no + self.category_name + '*'*(stars_no+extra) + '\n'

        for item in self.ledger:
            space_no = 30
            description = item['description'][:23]
            amount = str("{:.2f}".format(item['amount']))[:7]
            space_no -= len(description) + len(amount)
            result += description + ' '*space_no + amount + '\n'

        result += f'Total: {self.amount}'

        return result


# def create_spend_chart(categories = []):
#     result = 'Percentage spent by category\n'
#     percent = [x.spent for x in categories]
#     sum_percent = sum(percent)
#     percent = [round(x/sum_percent*100) for x in percent]
#     i = 100
#     while i >= 0:
#         i_str = str(i)
#         result += ' '*(3-len(i_str)) + i_str + '| '
#         for perc in percent:
#             if perc/10 <= 5: perc -= perc%10
#             else: perc += perc%10
#             if perc >= i: result += 'o  '
#             else: result += '   '
#         result += '\n'
#         i -= 10
#     result += '    ' + '-'*(len(categories)*3+1) + '\n'
#     i = 0
#     category_str = ''
#     max_category_length = max(len(ele.category_name) for ele in categories)
#     while i in range(max_category_length):
#         category_str += ' '*5
#         for ele in categories:
#             if i in range(len(ele.category_name)):
#                 category_str += ele.category_name[i] + '  '
#             else: category_str += '   '
#         if i <= max_category_length-2:
#           category_str += '\n'
#         i += 1
#     result += category_str
#     return result

def create_spend_chart_dict(categories = []):
    result = 'Percentage spent by category\n'
    data = dict([(x.category_name, x.spent) for x in categories])
    sum_percent = sum(data.values())
    for cat in data:
        perc = round(data[cat]/sum_percent*100)
        if perc/10 <= 5: perc -= perc%10
        else: perc += perc%10
        data[cat] = perc
    i = 100
    while i >= 0:
        i_str = str(i)
        result += ' '*(3-len(i_str)) + i_str + '| '
        for perc in data.values():
            if perc >= i: result += 'o  '
            else: result += '   '
        result += '\n'
        i -= 10
    result += '    ' + '-'*(len(categories)*3+1) + '\n'
    i = 0
    category_str = ''
    category_names = data.keys()
    max_category_length = max(len(key) for key in category_names)
    while i in range(max_category_length):
        category_str += ' '*5
        for name in category_names:
            if i in range(len(name)):
                category_str += name[i] + '  '
            else: category_str += '   '
        if i <= max_category_length-2:
          category_str += '\n'
        i += 1
    result += category_str
    return result


food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart_dict([business, food, entertainment]))