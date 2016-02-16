import random

class Person(object):
    # init a Person
    def __init__(self, name = "John Doe", height = 6.0, age = 21):
        self.name = name
        self.height = height
        self.age = age

class Teller(Person):
    # init a Teller
    def __init__(self, name = "John Doe", height = 1.7, age = 21, empNum = 123456, yrsWorked = 1):
        Person.__init__(self, name, height, age)
        self.empNum = empNum
        self.yrsWorked = yrsWorked

    # string representation of a Teller, format as follows:
    # "Name: John Doe, Emp Number: 123456, Years at bank: 1"
    def __str__(self):
        return "Name: " + str(self.name) + ", Emp Number: " + str(self.empNum) + ", Years at bank: " + str(self.yrsWorked)

class Bank(object):

    # init a Bank, all accounts start with no money
    def __init__(self, numAccounts, name = "People's Bank", location = "Austin TX", tellers = []):
        self.accounts = []
        for i in range(numAccounts):
            self.accounts.append(0.0)

        self.name = name
        self.location = location
        self.tellers = tellers

    # deposit the given amount of money into the specified account
    # returns true if deposit was successful, false otherwise
    def depositMoney(self, accountNumber, amount):
        if accountNumber > len(self.accounts):
            return False
        self.accounts[accountNumber] += amount
        return True

    # returns total value of the bank
    def getTotalAccounts(self):
        totalValue = 0.0
        for value in self.accounts:
            totalValue += value
        return totalValue

    # adds the given teller to the list of Tellers
    def hireTeller(self, teller):
        self.tellers.append(teller)

    # returns whether or not a teller of the given name works at the bank
    def tellerWorksHere(self, name):
        for teller in self.tellers:
            if teller.name == name:
                return True
        return False

    # string representation of a Bank, format as follows:
    # "People's Bank, Austin TX. Employees: 4, total value: $123456"
    def __str__(self):
        return str(self.name) +", " + str(self.location) + ". Employees: " + str(len(self.tellers)) + ", total value: $" + str(self.getTotalAccounts())

def main():
    # make a Wells Fargo located in Austin TX with 10 accounts
    wellsFargo = Bank(10, "Wells Fargo", "Austin TX")

    # hire the following tellers at Wells Fargo:
   
    # Erica, 1.5m tall, 28 years old, employee number: 7864, worked at Wells Fargo for 3 years
    # Jim, 1.8m tall, 32 years old, employee number: 2761, worked at Wells Fargo for 8 years
    # Michael, 1.65m tall, 17 years old, employee number: 3354, worked at Wells Fargo for 1 year
    wellsFargo.hireTeller(Teller("Erica", 1.5, 28, 7864, 3))
    wellsFargo.hireTeller(Teller("Jim", 1.8, 32, 2761, 8))
    wellsFargo.hireTeller(Teller("Michael", 1.65, 17, 3354, 1))
    
    # deposit $100 into 5 of the accounts chosen at random
    for i in range(5):
        wellsFargo.depositMoney(random.randint(0, 9), 100)

    # print out the bank
    print(str(wellsFargo))

main()

