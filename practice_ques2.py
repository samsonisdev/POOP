# Practice Question 2:
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        previous_balance = self.balance
        self.balance -= amount
        print("Previous Balance:", previous_balance, "Amount Debited:", amount, "Current Balance:", self.balance)

    def credit(self, amount):
        balance = self.balance
        self.balance += amount
        print("Previous Balance:", balance, "Amount Credited:", amount, "Current Balance:", self.balance)



customer_1 = Account(50000, 123)
customer_1.debit(20000)
customer_1.credit(10000)
customer_1.credit(20000)
