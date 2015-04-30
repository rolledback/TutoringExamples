import math

def is_prime(num):
    max_div = int(math.sqrt(num))
    for i in range(2, max_div + 1):
        if num % i == 0 and num != i:
            return False
    return True

def add_primes(n):
    if n == 1:
        return 0
    if is_prime(n):
        return n + add_primes(n - 1)
    else:
        return add_primes(n - 1)

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

def get_price(item):
    cat_result = catalog[item]
    if type(cat_result) == type(()):
        cost = 0
        for i in cat_result:
            cost += get_price(i)
        return cost
    if type(cat_result) == type(int()):
        return cat_result

print(add_primes(10))

init_catalog()
print(get_price('pizza'))
