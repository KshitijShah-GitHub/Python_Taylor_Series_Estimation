"""
Programmed By: Kshitij Shah
Date: April 14th 2018
Desc: This module is program to estimate functions e^x, cos(x), sin(x)
to user inputted digits of precision.
Motivation: because python's math module's constant 'e' is
only given to 15 digits after the decimal of precision, This method works for
many many more digits. I believe this code is worst case O(n^3), the nested
loops have potential for being optimized.
"""
from typing import Tuple, Dict
from decimal import Decimal, getcontext

factorial_dict = {0: 1, 1: 1, 2: 2}  # global var so repeated calls of different
# funcs don't redundantly calc factorials since TSeries uses factorials A LOT

sin_dict: Dict[int, Decimal] = {}  # will contain {precision: value} to prevent
cos_dict: Dict[int, Decimal] = {}  # calculating already calced vals, which is
e_dict: Dict[int, Decimal] = {}    # is always cool to have


def estimate_sin(val: Tuple[Decimal, int]) -> Decimal:
    """
    Input: Tuple of x value in Decimal format and digits of precision > 0  (int)
    Desc: Use Taylor Series to estimate sin(x) to input digits of precision.
    To prevent over precise estimation, use Alternating Series Test to determine
    whether current partial sum is accurate enough
    Output: Decimal format with expected precision.
    Note: The Taylor series works for all x in the set of Real numbers

    >>> from math import pi
    >>> estimate_sin((Decimal(pi), 5))
    0.00000
    """
    x = Decimal(val[0])
    precision = val[1]
    getcontext().prec = precision + 2

    if precision in sin_dict:
        return sin_dict[precision]
    else:
        kth_sum = Decimal(0)
        k_minus_1_sum = Decimal("-inf")
        i = 0
        precision_test = Decimal(1) / Decimal(10 ** precision)
        while abs(kth_sum - k_minus_1_sum) >= precision_test:
            k_minus_1_sum = kth_sum
            kth_sum = 0
            i += 1
            for j in range(i):
                a = Decimal(2 * j) + Decimal(1)
                kth_sum += \
                    (Decimal(-1) ** j * Decimal(x ** a)) / Decimal(factorial(a))
        sin_dict[precision] = (round(kth_sum, precision))

    return sin_dict[precision]


def estimate_cos(val: Tuple[Decimal, int]) -> Decimal:
    """
    Input: Tuple of x value in Decimal format and digits of precision > 0  (int)
    Desc: Use Taylor Series to estimate cos(x) to input digits of precision.
    To prevent over precise estimation, use Alternating Series Test to determine
    whether current partial sum is accurate enough
    Output: Decimal format with expected precision.
    Note: The Taylor series works for all x in the set of Real numbers

    >>> from math import pi
    >>> estimate_cos((Decimal(pi), 5))
    -1.00000
    """
    x: Decimal = Decimal(val[0])
    precision: int = val[1]
    getcontext().prec = precision + 2

    if precision in cos_dict:
        return cos_dict[precision]
    else:
        kth_sum = Decimal(0)
        k_minus_1_sum = Decimal("-inf")
        i = 0
        precision_test = Decimal(1) / Decimal(10 ** precision)
        while abs(kth_sum - k_minus_1_sum) >= precision_test:
            k_minus_1_sum = kth_sum
            kth_sum = 0
            i += 1
            for j in range(i):
                a = Decimal(2 * j)
                kth_sum += \
                    (Decimal(-1) ** j * Decimal(x ** a)) / Decimal(factorial(a))
        cos_dict[precision] = (round(kth_sum, precision))

    return cos_dict[precision]


def estimate_e(val: Tuple[Decimal, int]) -> Decimal:
    """
    Input: Tuple of x value in Decimal format and digits of precision > 0  (int)
    Desc: Use Taylor Series to estimate e^(x) to input digits of precision.
    To prevent over precise estimation, use Alternating Series Test to determine
    whether current partial sum is accurate enough
    Output: Decimal format with expected precision.
    Note: The Taylor series works for all x in the set of Real numbers

    >>> estimate_e((Decimal(1), 5))
    2.71828
    """
    x = val[0]
    precision = val[1]
    getcontext().prec = precision + 2

    if precision in e_dict:
        return e_dict[precision]
    else:
        kth_sum = 0
        k_minus_1_sum = Decimal("-inf")
        i = 0
        precision_test = Decimal(1) / Decimal(10 ** precision)
        while abs(kth_sum - k_minus_1_sum) >= precision_test:
            k_minus_1_sum = kth_sum
            kth_sum = 0
            i += 1
            for j in range(i):
                kth_sum += Decimal(x ** j) / Decimal(factorial(j))
        e_dict[precision] = Decimal(round(kth_sum, precision))

    return e_dict[precision]


def factorial(n: int) -> int:
    """
    Calculate the factorial for a integer input using memoized global dictionary
    to save time because Taylor Series sums calculate factorials frequently
    and usually in some incremental order
    """
    if n in factorial_dict:
        return factorial_dict[n]
    else:
        factorial_dict[n] = n * factorial(n - 1)

    return factorial_dict[n]


def get_input() -> Tuple[Decimal, int]:
    """
    Input: No input
    Desc: Get valid integer input for which to approximate value of function
    and how accurate to approximate the value to.
    The accuracy can't be too high because factorials get big real quick
    """
    x, n = None, None
    while not isinstance(n, int) or not isinstance(x, Decimal) or n <= 0:
        try:
            x = Decimal(float(input("Pick an x value to estimate function at: ")))
            n = int(float(input("How many decimal places do you need to "
                                "estimate to? (int value): ")))
        except ValueError:
            print("Please enter an integer value for precision and a float or "
                  "int for x value. ")
        if n <= 0:
            print("Make sure precision is more than 0")
    return (x, n)


if __name__ == "__main__":
    """
    This will take input of function or exit in form of a loop, replicating
    switch statements in other languages (like Java)
    """
    print("\nWelcome to the Taylor Series Estimator by Kshitij Shah!")
    print("Estimate one of the following 3 functions to a specified precision")
    exit_flag = False
    while not exit_flag:
        print("\nWhich function would you like to estimate? \n\
               1  sin(x) \n\
               2  cos(X) \n\
               3  e^x \n\
               4  Exit")
        in_str = "What would you like to estimate? "
        input_flag = False
        while not input_flag:
            sel = input(in_str).lower().strip()
            if sel == '4' or sel == 'exit':
                print("Thanks for using my script :)")
                input_flag = True
                exit_flag = True
            elif sel == '2' or 'cos' in sel:  # cos first in case of 'cosine'
                input_flag = True
                print("Estimating cos(x):")
                print(estimate_cos(get_input()))
            elif sel == '1' or 'sin' in sel:  # not cosine confirmed
                input_flag = True
                print("Estimating sin(x):")
                print(estimate_sin(get_input()))
            elif sel == '3' or sel == 'e^x' or sel == 'e' or sel == 'e^(x)':
                input_flag = True  # 'e' in sel is too permisive
                print("Estimating e^(x):")
                print(estimate_e(get_input()))
            else:  # default case
                print("invalid input, try a number (1 to 4) or the name "
                      "of the function like 'sin', 'cos' or 'e'\n")
