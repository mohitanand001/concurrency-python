from zero_even_odd import ZeroEvenOdd
from threading import Thread

import sys


def print_zero(x):
    if x != 0:
        raise Exception("You passed x={} which is not zero to print_zero in zero thread".format(x))
    print(x, end='')


def print_even(x):
    if x % 2 != 0 or x == 0:
        raise Exception("You passed x={} which is not an even number to print_even in even thread".format(x))
    print(x, end='')


def print_odd(x):
    if x % 2 != 1:
        raise Exception("You passed x={} which is not an odd number to print_odd in odd thread".format(x))
    print(x, end='')


n = int(sys.argv[1])
solution = ZeroEvenOdd(n)

Thread(target=lambda : solution.zero(print_zero)).start()
Thread(target=lambda : solution.even(print_even)).start()
Thread(target=lambda : solution.odd(print_odd)).start()


