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

def print_difference(result):
     if (result - (pi / 2)) > -0.0000000001 and (result - (pi / 2)) < 0:
         print("diff = 0.0000000000")
     else:
         print("diff = %.10f" % (result - (pi / 2)))

def rectangle_method(num):
    result = 0
    for loop in range(10000):
        val = 0 + loop * ((5000 - 0) / 10000)
        result += calculator(val, num)
    result *= ((5000 - 0) / 10000)
    print("Rectangles:")
    print("I%d = %.10f" % (num, result))
    print_difference(result)

def trapez_method(num):
    result = 0
    for loop in range(1, 10000):
        val = 0 + loop * ((5000 - 0) / 10000)
        result += calculator(val, num)
    result *= 2
    result += calculator(0, num) + calculator(5000, num)
    result *= (((5000 - 0) / 10000) / 2)
    print("\nTrapezoids:")
    print("I%d = %.10f" % (num, result))
    print_difference(result)

def simpson_method(num):
    tmp = 0
    result = 0
    for loop in range(0, 10000):
        val = 0 + loop * ((5000 - 0) / 10000)
        val += (((5000 - 0) / 10000) / 2)
        tmp += calculator(val, num)
    tmp *= 4
    for loop in range(1, 10000):
        val = 0 + loop * ((5000 - 0) / 10000)
        result += calculator(val, num)
    result *= 2
    result += tmp
    result += calculator(0, num) + calculator(5000, num)
    result *= (((5000 - 0) / 10000) / 6)
    print("\nSimpson:")
    print("I%d = %.10f" % (num, result))
    print_difference(result)
