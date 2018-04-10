##
## EPITECH PROJECT, 2018
## 110borewein_2017
## File description:
## calculation methods functions
##

from math import *

def calculator(val, frange):
    result = 1
    if val == 0:
        return 1
    for loop in range(frange + 1):
        divider = 2 * loop + 1
        result *= sin(val / divider) / (val / divider)
    return result

def rectangle_method(num):
    result = 0
    for loop in range(10000):
        val = 0 + loop * ((5000 - 0) / 10000)
        result += calculator(val, num)
    result *= ((5000 - 0) / 10000)
    print("Rectangles:")
    print("I%d = %.10f" % (num, result))
    if (result - (pi / 2)) > -0.0000000001 and (result - (pi / 2)) < 0:
        print("diff = 0.0000000000\n")
    else:
        print("diff = %.10f\n" % (result - (pi / 2)))
