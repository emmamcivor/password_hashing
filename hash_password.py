#!/usr/bin/python3.8

import hashlib
import binascii
import copy
import numpy as np

def convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,digest_hash):
    ''' This function takes a bytes object (list of integers between 0 and 255) and converts them into characters from a defined set of characters. 

Inputs
=====
min_acceptable_decimal: decimal number (between 0 and 255) representing the start of the character set
max_acceptable_decimal: decimal number (between 0 and 255) representing the end of the character set
digest_hash: the bytes object that we want to convert from bytes into characters

Outputs
=====
char_str: a string of characters that represents the digest_hash
'''
    char_str = ''
    mod_number = max_acceptable_decimal - min_acceptable_decimal + 1
  
    for i in range(len(digest_hash)):
        decimal_int = digest_hash[i]
        decimal_int_mod = decimal_int%mod_number
        adjusted_decimal_int = decimal_int_mod + min_acceptable_decimal
        char = chr(adjusted_decimal_int)
        char_str += char

    return char_str 

def substitute_chars(password):
    ''' I want to substitute the following characters:
[ --> !
\ --> %
] --> &
` --> *

Inputs
=====
password: hashed password with characters in allowed range

Outputs
password: hashed password with characters in user-defined range
======
new_password: with special characters substituted '''

    password_0 = password.replace('[','!')
    password_1 = password_0.replace('\\','%')
    password_2 = password_1.replace(']','&')
    new_password = password_2.replace('`','*')
    
    return new_password

def is_char_special(character):
    ''' I want to check whether a character is a special symbol

input: character
output: special_char-query = True, False (Boolean)
'''
    min_ord_special_1 = 33
    max_ord_special_1 = 47
    min_ord_special_2 = 58
    max_ord_special_2 = 64
    min_ord_special_3 = 91
    max_ord_special_3 = 96

    if min_ord_special_1<=ord(character)<=max_ord_special_1:
        special_char_query = True
    elif min_ord_special_2<=ord(character)<=max_ord_special_2:
        special_char_query = True
    elif min_ord_special_3<=ord(character)<=max_ord_special_3:
        special_char_query = True
    else:
        special_char_query = False
    
    return special_char_query

def password_contains_special_char(password):
    ''' I want to check whether the hashed password contains at least one special character


input: password
output: True, False (Boolean)
'''

    password_special_char_query = []
    
    for char in password:
        special_char_query = is_char_special(char)
        password_special_char_query.append(special_char_query)


    return any(password_special_char_query)

def update_password_special_character(password, max_acceptable_decimal):
    ''' I want to modfiy the final character in the password to be a special character if there are no special characters in the password'''

    char = password[-1]
    mod_number = max_acceptable_decimal+1

    while is_char_special(char)==False:
        char = chr((ord(char)+10)%mod_number)

    new_password = password[0:-1] + char

    return new_password

def SHA256_hash(general, salt):
    ''' This function uses SHA256 to create a hash.

Inputs
======
general: This is a string which contains the reference phrase for the password. This contains a string prefaced by b.
salt: This is a string which contains a piece of random data for the password. This contains a string prefaced by b.

Outputs
======
password: This is a string of length 12 which is an ascii representation of the hash digest
'''

    general_byte = general.encode()
    salt_byte = salt.encode()

    digest_hash = hashlib.sha256(general_byte+salt_byte).digest()

    min_acceptable_decimal = 33
    max_acceptable_decimal = 122
    char_str = convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,digest_hash)

    password = char_str[0:12]
    new_password = substitute_chars(password)

    return new_password
