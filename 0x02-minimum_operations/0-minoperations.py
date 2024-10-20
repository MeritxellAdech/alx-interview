#!/usr/bin/python3
"""
Define a function to find the minimum operations
to copy all and paste a character.
"""


def minOperations(n):
    """
    Determines the minimum number of operations
    to perform character duplication.

    Parameters:
        n : int
        The number of time to duplicate
        the character in the text editor.

    Returns:
        The minimum number of steps to perform
        all operations resulting in `n`
        characters of the letter in the text
        editor.
    """
    factors = [1]
    tmp_results = []
    len_of_factors = 0
    median = 0

    if n <= 1:
        return 0

    tmp_results = [incr for incr in range(2, n) if n % incr == 0]
    if n < 6 or not tmp_results:
        return n
    factors.extend(tmp_results)
    factors.append(n)

    len_of_factors = len(factors)
    median = int(len_of_factors / 2)

    if len(factors) % 2 != 0:
        return factors[median] * 2
    return factors[median] + factors[median - 1]
