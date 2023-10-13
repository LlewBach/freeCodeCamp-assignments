from math import floor

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        result = self.check_funds(amount)
        if result:
            self.ledger.append({"amount": (amount * -1), "description": description})
        return result
    
    def get_balance(self):
        balance = 0
        for obj in self.ledger:
            balance += obj["amount"]
        return balance
    
    def transfer(self, amount, cat):
        result = self.check_funds(amount)
        if result:
            self.withdraw(amount, description=f"Transfer to {cat.name}")
            cat.deposit(amount, description=f"Transfer from {self.name}")
        return result
    
    def check_funds(self, amount):
        balance = 0
        for obj in self.ledger:
            balance += obj["amount"]
        if amount > balance:
            return False
        else:
            return True
        
    def __str__(self):
        chars_left = 30 - len(self.name)
        before_stars = floor(chars_left / 2)
        after_stars = chars_left = before_stars
        title = f"{'*' * before_stars}{self.name}{'*' * after_stars}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            amt = amt[:7]
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"

        return title + items + total
    
    def amount_spent(self):
        spent = 0
        for record in self.ledger:
            if record["amount"] < 0:
                spent += record["amount"]
        return abs(spent)
                

            
def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculating %s
    cat_names = []
    cat_spending = []
    cat_percents = []
    for category in categories:
        cat_names.append(category.name)
        spending = category.amount_spent()
        cat_spending.append(spending)
    
    total_spent = sum(cat_spending)
    for amount in cat_spending:
        cat_percents.append((((amount / total_spent) * 100) // 10) * 10)
    # Chart body
    chart_lines = ""
    for i in range(11): 
        percent_label_num = 100 - (10 * i)
        o_string = ""
        for cat_percent in cat_percents:
            if cat_percent >= percent_label_num:
                o_string += " o "
            else:
                o_string += "   "
        
        percent_label_string = str(percent_label_num)
        if len(percent_label_string) == 3:
            chart_lines += f"{percent_label_num}|{o_string} \n"
        elif len(percent_label_string) == 2:
            chart_lines += f" {percent_label_num}|{o_string} \n"
        elif len(percent_label_string) == 1:
            chart_lines += f"  {percent_label_num}|{o_string} \n"

    # Graph x axis
    dash_number = len(cat_names) * 3 + 1
    x_axis = f"    {'-' * dash_number}\n"

    # Cat label strings
    longest_label = max(cat_names, key=len)
    labels = ""
    for i in range(len(longest_label)):
        letter_list = []
        for name in cat_names:
            if i == 0:
                letter_list.append(name[i].upper())
            else:
                try:
                    letter_list.append(name[i].lower())
                except IndexError:
                    letter_list.append(" ")
        
        letter_line = f"{' ' * 4}"
        for letter in letter_list:
            letter_line += f" {letter} "
        letter_line += " "
        labels += f"{letter_line}\n"

    return title + chart_lines + x_axis + labels.rstrip('\n')

# Testing ========================================

food = Category("food")
food.deposit(900, "deposit")
food.withdraw(105.55)

entertainment = Category("entertainment")
entertainment.deposit(900, "deposit")
entertainment.withdraw(33.40)

business = Category("business")
business.deposit(900, "deposit")
business.withdraw(10.99)


print(create_spend_chart([food, entertainment, business]))










