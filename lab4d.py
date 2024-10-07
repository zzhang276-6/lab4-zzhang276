#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Place code here - refer to function specifics in section below
    return string[:5]
def last_seven(string):
    # Place code here - refer to function specifics in section below
    return string[-7:]
def middle_number(number):
    # Place code here - refer to function specifics in section below
    number_str = str(number)
    return number_str[1:3]
def first_three_last_three(s1,s2):
    # Place code here - refer to function specifics in section below
        return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
