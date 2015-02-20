# Created 2/20/2015
# Demonstrates while loops in Python
# Run with: Python 2.7

import random
import time

'''
While loops are most often used when you wish to 
iterate but do not know how many times you want to do 
so. For example, the statement "check on the cookies 
every 5 min until they are brown" could be considered a 
good example for a while loop. The act of checking the cookies
is based on some condition, not any sort of number. That 
being said, while loops can easily be used to iterate in 
a counting type of situation.
'''

# main function
def main():
    # while loop which just counts numbers
    m = 0
    while m < 6:
        print("m: " + str(m))
        m = m + 1 # don't forget to increment any counting variables

    # while loop which is based more so on a condition
    n = 0
    tries = 0
    while n != 50:
        n = random.randint(0, 50)
        tries = tries + 1
    print("\nFound 50 in " + str(tries) + " tries!\n")

    # another while loop which isn't very iterative
    curr_time = int(time.time())
    while curr_time % 10 != 0:
        print("Current time is: " + str(curr_time))
        time.sleep(1)
        curr_time = int(time.time())
    print("Final time: " + str(curr_time))
    
main()
