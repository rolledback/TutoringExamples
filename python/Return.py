# Created 2/21/2015
# Demonstrates use of return in Python
# Run with: Python 2.7 or 3.4

'''
The return keyword is essential in both Python and 
many other programming languages. Return allows you to 
pass a value back from a function, to the place in code 
where the function was called. In other words you "return" 
the value. Although the use of return is quite simple, the 
concepts behind it can be difficult to master. 
'''

# function that returns a value
def add_one(num):
    return num + 1

# you can have multiple returns in a function
def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        return False

# as soon as a return statement is executed, you 
# leave the function and no more code is ran
def foo():
    return 10
    print("This is never ran.")

# main function
def main():
    # simple case of using return
    x = add_one(9)
    print("9 + 1 = " + str(x))

    # a returned value can immediately be used as an argument 
    # for another function
    print("Is 10 even? " + str(is_even(10)))
    print("Is 15 even? " + str(is_even(15)))

    # demonstrate concept behind the foo function
    print("Foo returns: " + str(foo()))

    # even if a function returns a value, you don't have to use it
    add_one(15)

main()
