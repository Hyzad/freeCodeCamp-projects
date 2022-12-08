class Category:
    total = 0
    def __init__(self, z):
        self.category = z
        self.ledger = []
        self.total = 0
        print(self.category)

    def deposit(self, amount, description=""): # allows deposits into each category
        self.dep_amount = amount
        self.description = description
        Category.total = Category.total + self.dep_amount # updates the total amount deposited
        self.total += self.dep_amount
        ledg = {'amount':self.dep_amount, 'description':self.description}
        self.ledger.append(ledg)
        self.dep_total = 0
        self.dep_total = self.dep_total + self.dep_amount
        
        #print(self.ledger)
    
    def withdraw(self, amount, description=""): #allows withdrawals 
        
        balance_check = self.check_funds(amount)
        #print(balance_check) # need to check balance here
        if balance_check == False:
            return False
        else:
            self.with_amount = 0 - amount
            self.description = description
            Category.total = Category.total + self.with_amount
            self.total += self.with_amount
            ledg = {'amount': self.with_amount, 'description': self.description}
            self.ledger.append(ledg)
            self.with_total = 0
            self.with_total = self.with_total + self.with_amount
            return True

    def get_balance (self): # shows balance of the category specified something is wrong here
        balance = self.total
        return balance

    def transfer (self, amount, category): # transfers money between categories
        self.transf_amount = amount
        #print(self.transf_amount)
        name = category.category

        balance_check = self.check_funds(self.transf_amount)

        from_desc = f"Transfer from {self.category}"
        to_desc = f"Transfer to {name}"

        if balance_check == True:
            self.withdraw(amount=self.transf_amount, description=to_desc)
            category.deposit(amount=amount, description=from_desc)
            return True
        else:
            print("no")
            return False

    # checks whether the amount in the category is less than the specified amount
    def check_funds(self, amount):
        self.check_amount = amount

        if self.check_amount > self.total:
            return False
        else:
            return True
    
    def __repr__(self):
        title = len(self.category)
        if title % 2 == 1:
            stars = 15 - (title//2)
            end_stars = stars - 1
            header = stars*"*" + self.category + end_stars*"*"
        else:
            stars = 15 - (title//2)
            header = stars*"*" + self.category + stars*"*"
        
        item = []
        width = 30
        for i in range(0, len(self.ledger)):
            for j, k in self.ledger[i].items():
                item.append(k)
        transactions = []
        for i in range(0, len(item), 2):
            # formats the numbers to be a string with 2 d.p
            format_float = "{:.2f}".format(item[i])
            #appends the descrpition followed by the ammount justified to the right
            transactions.append(
                (str(item[i+1][0:23]) + format_float.rjust(width-len(item[i+1][0:23]))))
        # joins each item in transactions with a new line
        transaction_list = "\n".join(transactions)
        format_total = "{:.2f}".format(self.total)
        total = "Total: " + format_total  # total amount

        return header + "\n" + transaction_list + "\n" + total





def create_spend_chart(categories):
    category_name = []
    category_amount = []
    for i in categories:
        category_name.append(i.category)
        category_amount.append(i.with_total)
    proportion = []
    for i in range(0, len(category_amount)):
        proportion.append(round((category_amount[i] / sum(category_amount)) * 100)//10)
    
    header = "Percentage spent by category"
    width = len(categories) * 3 +1
    bottom_dash = " " * 4 + "-" * width
    row = []
    for i in range(0,11):
        gap = 3 - len(str(i * 10))
        space = " " * gap
        row.append(space + str(i*10) + "|")

    mark = " o "
    spaces = "   "


    for j in range(len(proportion)):
        i = 0
        while i < 11:
            if i <= proportion[j]:
                row[i] += mark
            else:
                row[i] += spaces
            i += 1

    for i in range(len(row)):
        row[i] = row[i] + " "

    row = list(reversed(row))
    row.append(bottom_dash)

    category_length = len(max(category_name, key=len))

    for i in range(len(category_name)):
        category_name[i] = category_name[i] + " "*(category_length-len(category_name[i]))

    name_label = []

    for i in range(0, category_length):
        name_label.append(" "*4)
        for j in category_name:
            name_label[i] += " " + j[i] + " "
    for i in range(category_length):
        name_label[i] += " "
    chart = row + name_label
    chart.insert(0, header)

    
    return "\n".join(chart)