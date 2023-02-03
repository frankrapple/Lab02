#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''

    def is_even(n):
        return n % 2 == 0

    new_function = is_even

    evens2 = list(filter(new_function, range(0, n+1)))
    return evens2
