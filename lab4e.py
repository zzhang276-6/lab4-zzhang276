#!/usr/bin/env python3
# Author ID: zzhang276

def is_digits(sobj):
    # place code here - loop through each character in sobj
    for char in sobj:
        if not char.isdigit():
        #if char not in '0123456789':
            return False
    return True
if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
