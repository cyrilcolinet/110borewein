##
## EPITECH PROJECT, 2018
## 110borewein_2017
## File description:
## utils file
##

import sys

def print_help():
    print("USAGE:")
    print("\t./110borewein <num>\n")
    print("DESCRIPTION:")
    print("\tnum\tconstant defining the integral to be computed")

def initialize():
    try:
        num = int(sys.argv[1])
    except (Exception) as err:
        print(err)
        sys.exit(84)
    if num < 0:
        print("The number must be a positive number.")
        print("Usage: ./110borewein <num>")
        sys.exit(84)
    return num

def check_arguments():
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)
    elif len(sys.argv) != 2:
        print("Invalid arguments number.")
        print("Usage: ./110borewein <num>")
        sys.exit(0)
