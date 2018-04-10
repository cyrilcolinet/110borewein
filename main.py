#!/usr/bin/env python

##
## EPITECH PROJECT, 2018
## 110borewein_2017
## File description:
## main file 110borewein
##

import sys
from utils import *
from methods import *

def borewein():
    num = initialize()
    rectangle_method(num)
    trapez_method(num)
    simpson_method(num)

def main():
    check_arguments()
    borewein()

if __name__ == '__main__':
    main()
