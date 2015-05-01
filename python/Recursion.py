import math

# Created 4/30/2015
# Demonstrates basic recursive functions in Python
# Run with: Python 2.7 or 3.4

'''
Recursion is a powerful programming paradigm in which you break
a problem into smaller instances of the problem until you are left
with a problem that you can solve. You can then use these small solutions
to recreate solutions to the subproblems, and eventually to
find a solution for your original solution. Many different problems
can have recursion applied to them so it is important to understand
how it works.
'''

# determines if a number is prime
def is_prime(num):
    max_div = int(math.sqrt(num))
    for i in range(2, max_div + 1):
        if num % i == 0 and num != i:
            return False
    return True

# adds up all primes <= n
def add_primes(n):
    if n <= 1:
        return 0
    if is_prime(n): # n is prime, so add it to whatever primes are below it
        return n + add_primes(n - 1)
    else:
        return add_primes(n - 1) # n was not prime, so return the sum of primes below n

# inits a dictionary of items which are either made up other items
# or which have a set cost
catalog = {}
def init_catalog():
    catalog['computer'] = ('mouse', 'screen', 'keyboard', 'tower')
    catalog['car'] = ('tire', 'tire', 'tire', 'tire', 'seat', 'engine')
    catalog['pizza'] = ('crust', 'cheese', 'sauce')
    catalog['tower'] = ('hard drive', 'CPU')
    catalog['engine'] = ('fuel tank', 'spark plug')
    catalog['crust'] = ('yeast', 'flour')

    catalog['mouse'] = 15
    catalog['screen'] = 250
    catalog['keyboard'] = 50
    catalog['hard drive'] = 200
    catalog['CPU'] = 150
    
    catalog['tire'] = 45
    catalog['seat'] = 225
    catalog['fuel tank'] = 300
    catalog['spark plug'] = 15

    catalog['yeast'] = 5
    catalog['flour'] = 2
    catalog['cheese'] = 8
    catalog['sauce'] = 10

# gets the price of a given item by recursively traversing the catalog
def get_price(item):
    cat_result = catalog[item]
    if type(cat_result) == type(()): # the items value in the catalog was a list of items
        cost = 0
        for i in cat_result:
            cost += get_price(i)
        return cost
    if type(cat_result) == type(int()): # the items value in the catalog was a number
        return cat_result

for i in range(0, 10):
    print('Sum of primes 0 to', i, '=', add_primes(i))

print()
init_catalog()
print('Total cost to make a computer:', get_price('computer'))
print('Total cost to make a car:', get_price('car'))
print('Total cost to make a pizza:', get_price('pizza'))

