# Created 2/20/2015
# Demonstrates classes in Python
# Run with: Python 2.7

'''
Classes are used to hold values associated with "objects". This type 
of programming is referred to as Object Oriented Programming or OOP. Objects 
are very useful in modeling real world problems and thus make programming 
easier. Classes are primarialy made up of class functions, class variables 
and a constructor, all of which are demonstrated below.
'''

class Bank(object):

    # The __init__ function is your constructor, it is called every 
    # time you make a new object such as, "my_bank = Bank(...)". Constructors 
    # can also take arguments.
    def __init__(self, name, num_accounts):
        self.name = name
        self.num_accounts = num_accounts;
        self.accounts = []
        for i in range(0, self.num_accounts):
            self.accounts.append(0)

    # Classes can have functions, which must be called using an instance 
    # of the class, followed by the . operator, example: "my_bank.print_accounts()".
    def print_accounts(self):
        print('-----------------------')
        print('Status of All Accounts:')
        for i in range(0, self.num_accounts):
            print('Account ' + str(i) + ': $' + str(self.accounts[i]))
        print('-----------------------')

    # Notice that each class method has a "self" argument. This argument is 
    # added for you when you actually call the funtion. Its presence allows you 
    # to access class variables by using "self.var_name".
    def avg_account_balance(self):
        sum = 0
        for i in range(0, self.num_accounts):
            sum = sum + self.accounts[i]
        return sum / self.num_accounts

    # Other than that, class functions are fairly similar to normal functions. They 
    # can have arguments, return values, and need semicolons at the end of their 
    # definitions.
    def modify_account(self, acc_num, new_value):
        self.accounts[acc_num - 1] = new_value

def main():
    # using a constructor
    my_bank = Bank('Wells Fargo', 3)

    # examples of calling a class method
    my_bank.modify_account(1, 500);
    my_bank.modify_account(2, 483);
    my_bank.modify_account(3, 792);

    my_bank.print_accounts();

    print('\nAvg account value: ' + str(my_bank.avg_account_balance()) + '\n')

main()
