import os
import sys
import time
from colorama import Fore
#'notice: i am a beginner creating newbie scripts, requirements are in the text(to install just simply run pip3 -r requirements.txt install)'
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def multi(a, b):
    return a * b

def add(a, b):
    return a + b

def div(a, b):
    return a / b

def sub(a, b):
    return a - b

def addition():
    clear()
    print('addition')
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:   
        print("Invalid input. Please enter a number.")
    clear()
    print("=",
    add(a, b))
    input(Fore.CYAN + 'Press enter to Continue.' + Fore.LIGHTGREEN_EX)
    chosen()

def multiplication():
    clear()
    print('multiplication')
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:   
        print("Invalid input. Please enter a number.")
    clear()
    print("=",
    multi(a, b))
    input(Fore.CYAN + 'Press enter to Continue.' + Fore.LIGHTGREEN_EX)
    chosen()

def division():
    clear()
    print('division')
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:   
        print("Invalid input. Please enter a number.")
    clear()
    print("=",
    div(a, b))
    input(Fore.CYAN + 'Press enter to Continue.' + Fore.LIGHTGREEN_EX)
    chosen()

def substitution():
    clear()
    print('substitution')
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:   
        print("Invalid input. Please enter a number.")
    clear()
    print("=",
    sub(a, b))
    input(Fore.CYAN + 'Press enter to Continue.' + Fore.LIGHTGREEN_EX)
    chosen()


def tryagain():
    print('please try again')
    time.sleep(3)
    chosen()

def chosen():
    clear()
    print(Fore.LIGHTGREEN_EX)
    print('HAND SWORD 2023-2024 ver 1')
    print('')
    print('')
    print("1 for add, 2 for sub, 3 for multi, 4 for div")
    c = input('choose 1-4:')
    if c == '1':
        addition()
    elif c == '2':
        substitution()
    elif c == '3':
        multiplication()
    elif c == '4':
        division()
    else:
        print(Fore.RED + 'Out of Selection' + Fore.WHITE)
        Fore.RESET
        tryagain()



chosen()


 