# Define functions
# Take input
# Print Answers
import time
import sys

# For slow string
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1/10)

def add(x, y):
    ans = x + y
    return f'\n{x} + {y} = {ans}'


def sub(x, y):
    ans = x - y
    return f'\n{x} - {y} = {ans}'


def mul(x, y):
    ans = x * y
    return f'\n{x} * {y} = {ans}'


def div(x, y):
    ans = x / y
    return f'\n{x} / {y} = {ans}'

# while loop to keep the program running
def main():
    slowprint('\nWhat computaion you want to do?\n\nAddition: + \nSubtraction: - \nMultiplication: * \nDivision: / \nExit: x\n')
    choose = input('Enter an input: ')

    if choose == '+':
        slowprint('Enter the first value: ')
        x = int(input())
        slowprint('Enter the second value: ')
        y = int(input())
        slowprint(add(x, y))
    elif choose == '-':
        slowprint('Enter the first value: ')
        x = int(input())
        slowprint('Enter the second value: ')
        y = int(input())
        slowprint(sub(x, y))
    elif choose == '*':
        slowprint('Enter the first value: ')
        x = int(input())
        slowprint('Enter the second value: ')
        y = int(input())
        slowprint(mul(x, y))
    elif choose == '/':
        slowprint('Enter the first value: ')
        x = int(input())
        slowprint('Enter the second value: ')
        y = int(input())
        slowprint(div(x, y))
    elif choose == 'x':
        slowprint('Closing the program.')
        exit()

main()

while True:
    
    slowprint('\nWant to do another computation?')
    time.sleep(.7)
    user = int(input(('\nYes(1) or No(2)\n: ')))
    if user == 1:
        main()
    elif user == 2:
        slowprint('\nHope to see you again!')
        exit()
    else:
        slowprint('Sorry I can only accept Yes(1) or No(2)')
        user