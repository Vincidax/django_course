# functions
# print('a value')
# print(input('ask a value '))

#methods -> functions of datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('e','3'))

# new functions
# print(abs(-1))
# print(max(10,5))
# print(min(0,1))
# print(len('test'))
import math
width = float(input("Enter width: "))
height = float(input('Enter height: '))



def hypotenuse(width, height):
    hypo = math.sqrt(pow(width, 2) + pow(height,2))
    return hypo

print('The hypothenuse is', hypotenuse(width, height))