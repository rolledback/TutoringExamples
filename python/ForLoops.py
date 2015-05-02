# Created 2/20/2015
# Demonstrates for loops in Python
# Run with: Python 2.7 or 3.4

import random
import time

'''
For loops are used when you want to repeat a block of code
a set number of times. Most ofetn, for loops are used when going
through strings, lists, arrays, dictionaries, or other data
structures. In Python there are 2 main for loops which exist. Both
will be discussed here.
'''

# main function
def main():
    # The first type of for loop uses the range function
    # When only given one argument, range goes from 0 -> n - 1
    print('Print first 10 integers.')
    for i in range(10):
        print(i)

    # Notice the variable i, it is the variable the loop loops through
    # When given two arguments, range goes from m -> n - 1
    print('\nPrint 1 to 10.')
    for i in range(1, 11):
        print(i)

    # A third variable will change how much your looping variable
    # changes by at each iteraion (the default is +1)
    print('\nPrint even numbers between 0 and 11.')
    for i in range(0, 11, 2):
        print(i)

    # For loops are helpful for going through an indexed data structure
    nums = (3, 5, 7, 4, 8, 22, 57, 5, 2, 1)
    print('\nPrint the list one item at a time.')
    for i in range(10):
        print(nums[i])

    # The second type of for loop can be used to iterate through a data
    # structure's elements directly. Notice how the range function is
    # replaced with the name of the data structure.
    print('\nPrint the list item at a time.')
    for num in nums:
        print(num)

    # This for loop can also be used on other types of data structures
    sentence = 'The quick brown fox jumped over the lazy dog'
    print('\nThe letters in: ', sentence, '.')
    for letter in sentence:
        print(letter)

    colors = {}
    colors['RED'] = 2342
    colors['BLUE'] = 6431
    colors['GREEN'] = 3234


    print('\nContents of the dictionary.')
    for key in colors:
        print(key, '->', colors[key])


    
main()
