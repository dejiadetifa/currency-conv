
# create a python class
class Customer:
    bank_name = "GTBank"
    # constructor
    def __init__(self,first_name,last_name,gender,account_no=12345678,balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.account_no = account_no
        self.balance = balance

    # behavior
    def name(self):
        full_name = self.first_name + " " +self.last_name
        return full_name

    def checkBalance(self):
        balance = self.balance
        return balance



# object
customer_1 = Customer("John","Martins","M")
customer_2 = Customer(first_name = "Julianah", last_name = "Goldfish", gender = "F", account_no = 23546147)


#print("Customer name: {}".format(customer_1.name()))
#print("Customer name: {}".format(customer_2.name()))

#print("Customer Name: {}".format(customer_1.Bank name))
#print("Customer Name: {}".format(customer_.checkBalance()))

# to change bank name
Customer.bank_name = "Access bank"

print("Customer Name: {}".format(customer_1.first_name))
print("Bank Name: {}".format(customer_1.bank_name))