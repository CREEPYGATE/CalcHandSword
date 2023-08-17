import time
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def installreq():
    clear()
    print('Installing requirements...')
    print('')
    print('')
    if os.name == 'nt':
        os.system('color 04')
        os.system('pip install colorama')
    else:
        os.system('pip3 install colorama')

installreq()

