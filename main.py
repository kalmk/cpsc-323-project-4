# CPSC 323
# Project 4
from leader import *

if (__name__ == "__main__"):
    tac_code = {}

    # Read lines from input and store them
    with open('test_cases/test1.in', 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            tac_code[index + 1] = line

    # print(tac_code)

    leaders = find_leaders(tac_code)
    print(leaders)

