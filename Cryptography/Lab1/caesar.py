#!/usr/bin/env python3
# Caesar Cipher 1
from freq import xmod26
MAX_KEY_SIZE = 26


def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        modes = ['e', 'encrypt', 'd', 'decrypt']
        if mode in modes:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def getMessage():
    print("Enter your message")
    return input()


def getKey():

    while True:

        # print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input('Enter the key number : '))
        if key != 0:
            if key < 26:
                return xmod26(key)
            else:
                print("Number entered is greater than 26 converted to 1-26 is : ",xmod26(key))
                return(xmod26(key))
        else:
        	print('Enter number except 0 : ')
        # if (key >= 1 and key <= MAX_KEY_SIZE):
        #     return key


def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd':
        key = -key
    translated = ""

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


# mode = getMode()
# message = getMessage()
# key = getKey()

# print('text: ' + getTranslatedMessage(mode, message, key))