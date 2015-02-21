# Created 2/20/2015
# Demonstrates functions in Python
# Run with: Python 2.7 or 3.4

'''
Functions are simply independent blocks of code. You 
usually create functions so you can easily reuse or 
test a small set of code. To create a function in 
python, you start with the keyword def. This keyword 
is short for the word define. You then write the name 
of your function, followed by a set of parens, which can contain 
a list of arguments (or variables) which are passed to your
function when it is used. Finally, you finish the definition 
with a colon, similar to an if statement or loop.
'''

# determines if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# main function
def main():

    # prints out the primes from 1 to 10  
    print("\nPrimes in 1 through 10:")
    for n in range(1, 11):
        prime = True
        if n <= 1:
            prime = False
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime == True:
            print(n)

    # does the same thing, but uses a function
    print("\nPrimes in 1 through 10:")
    for n in range(1, 11):
        if is_prime(n):
            print(n)

main()
