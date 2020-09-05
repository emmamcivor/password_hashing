#!/usr/bin/python3.8

import hashlib
import binascii
import copy

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
======
new_password: with special characters substituted '''

    password_0 = password.replace('[','!')
    password_1 = password_0.replace('\\','%')
    password_2 = password_1.replace(']','&')
    new_password = password_2.replace('`','*')
    
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

    min_acceptable_decimal = 48
    max_acceptable_decimal = 122
    char_str = convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,digest_hash)

    password = char_str[0:12]
    new_password = 
substitute_chars(password)

    return new_password
