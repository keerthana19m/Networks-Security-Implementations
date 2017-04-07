import re
import sys
from itertools import cycle


def caesar(ptext, shiftkey):
    cipherText = ''
    for ch in ptext:
      position = ord(ch) + shiftkey
      if ch.islower():
        if position > ord('z'):
          position -= 26
        elif position < ord('a'):
          position += 26
      elif ch.isupper():
        if position > ord('Z'):
          position -= 26
        elif position < ord('A'):
          position += 26
      finalLetter = chr(position)
      cipherText += finalLetter
    print(cipherText)
    return cipherText


ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    keyptpairs = zip(plaintext, cycle(key))
    result = ''

    for pair in keyptpairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    print "Encrypted Text :", result.lower()
    return result.lower()


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    keyptpairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in keyptpairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    print "Decrypted Text :", result.lower()

    return result

def transposition(matrix, words):
    cipher = ''
    length = len(matrix)
    blanks = ''.join(' ' for i in range(length - 1))

    for x in range(0, len(words), length):
        item = words[ x : x + length ] + blanks
        for pos in matrix:
            cipher += item[pos - 1]
    print cipher.lower()
    return cipher.lower()


def reverse(matrix):
    length = len(matrix)
    arr = [0] * length
    for i in range(length):
        arr[matrix[i] - 1] = i + 1
    return arr

if __name__ == "__main__":
    print "--------------------------- CIPHER --------------------------------------\n"
    prompt = '> '
    print "PICK THE CIPHER YOU WANT TO EXECUTE:"
    filechoose = {}
    filechoose['1']="caser cipher" 
    filechoose['2']="vigenere cipher"
    filechoose['3']="matrix transposition cipher"
    validity = False
    while validity==False: 
        options=filechoose.keys()
        options.sort()
        for entry in options: 
            print entry, filechoose[entry]

        print"Please Select:1,2 or 3" 
        selection = raw_input(prompt)
        print "\n"
        if selection =='1': 
            print "you chose caesar cipher"
            selection = raw_input ("encrypt/decrypt: Please enter 'encrypt' or 'decrypt': ")
            if selection == 'encrypt':

              plainText = raw_input("\nWhat is your plaintext? ")
              shiftkey = (int(raw_input("What is your shiftkey? ")))%26
              caesar(plainText, shiftkey)

            else:
              decryptedtext = raw_input("\nWhat is your Encrypted Text? ")
              shiftkey = ((int(raw_input("What is your shiftkey? ")))%26)*-1
              caesar(decryptedtext, shiftkey)

            validity = True; 
        elif selection == '2': 
            print "you chose vigenere cipher"
            selection = raw_input ("encrypt/decrypt: Please enter 'encrypt' or 'decrypt': ")
            if selection == 'encrypt':

              plainText = raw_input("\nWhat is your plaintext? ")
              enc_key = raw_input("What is your key? ")
              encrypt(enc_key, plainText)

            else:
              decryptedtext = raw_input("\nWhat is your Encrypted Text? ")
              dec_key = raw_input("What is your key? ")
              decrypt(dec_key, decryptedtext)

            validity = True;
        elif selection == '3':
            print "you chose matrix transposition cipher" 
            selection = raw_input ("encrypt/decrypt: Please enter 'encrypt' or 'decrypt': ")
            if selection == 'encrypt':

              plainText = raw_input("\nWhat is your plaintext? ")
              str_arr = raw_input("What is your matriX? ").split(' ') 
              matrix = [int(num) for num in str_arr]
              transposition(matrix, plainText)

            else:
              decryptedtext = raw_input("\nWhat is your Encrypted Text? ")
              str_arr = raw_input("What is your matriX? ").split(' ') 
              matrix = [int(num) for num in str_arr]
              secret = reverse(matrix)
              transposition(secret, decryptedtext)

            validity = True;
        else: 
            print "Unknown Option Selected! Please enter valid input again \n" 
            validity = False;