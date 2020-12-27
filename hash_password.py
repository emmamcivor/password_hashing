#!/usr/bin/python3.8

import hashlib
import binascii
import copy
import numpy as np

def convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,digest_hash):
    ''' This function takes a bytes object (list of integers between 0 and 255) and converts them into characters. I have restricted the character set to a subset of the ASCII character set. Characters in this restricted set can be used in the password.

Inputs
=====
min_acceptable_decimal: decimal number (between 0 and 255) representing the start of the character set that will be used in the password
max_acceptable_decimal: decimal number (between 0 and 255) representing the end of the character set that will be used in the password
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
    ''' This function substitutes the following characters in a password:
` --> *

Inputs
=====
password: current set of characters in hashed password

Outputs
======
new_password: password with special characters substituted 
'''

    new_password = password.replace('`','*')
    
    return new_password

def is_char_special(character):
    ''' This function determines whether a character is a special symbol character.

inputs
======
character: single character 
outputs
======
special_char_query: Boolean (True or False) representation of the result of whether the input character is a special symbol
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
    ''' This function determines whether the password contains at least one special symbol character.


inputs
======
password: current set of characters in hashed password
outputs
======
Boolean (True, False) representation of the result of whether the password contains at least one special symbol character
'''

    password_special_char_query = []
    
    for char in password:
        special_char_query = is_char_special(char)
        password_special_char_query.append(special_char_query)


    return any(password_special_char_query)

def update_password_special_character(password, max_acceptable_decimal):
    ''' This function takes the final character in the password and if the character is not a special symbol character then the function iterates forwards by 10 places (up to the maximum of the character set) and the character is iterated over in this manner until the character is a special symbol character.

inputs
======
password: current set of characters in hashed password
max_acceptable_decimal: decimal number (between 0 and 255) representing the end of the character set that will be used in the password

outputs
======
new_password: password containing at least one special symbol character
'''

    char = password[-1]
    mod_number = max_acceptable_decimal+1

    while is_char_special(char)==False:
        char = chr((ord(char)+10)%mod_number)

    new_password = password[0:-1] + char

    return new_password

def ensure_password_contains_special_char(password, max_acceptable_decimal):
    ''' This function ensures that the password contains at least one special symbol character. First, the functions determines whether the password contains a special character. If the password contains a special character this password is returned. If the password does not contain a special character then the final character is modified to be a special character.

inputs
======
password: current set of characters in hashed password
max_acceptable_decimal: decimal number (between 0 and 255) representing the end of the character set that will be used in the password

outputs
======
new_password: password containing at least one special symbol character
'''

    password_query = password_contains_special_char(password)
    if password_query == False:
        new_password = update_password_special_character(password, max_acceptable_decimal)
    else:
        new_password = password

    return new_password    

def SHA256_hash(general, salt):
    ''' This function uses SHA256 to create a hashed password.

Inputs
======
general: This is a string which contains the reference phrase for the password. This contains a string prefaced by b.
salt: This is a string which contains a piece of random data for the password. This contains a string prefaced by b.

Outputs
======
final_password: This is a string of length 12 which is an ascii representation of the hash digest and contains at least one special symbol character
'''

    general_byte = general.encode()
    salt_byte = salt.encode()

    digest_hash = hashlib.sha256(general_byte+salt_byte).digest()

    min_acceptable_decimal = 33
    max_acceptable_decimal = 122
    char_str = convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,digest_hash)

    password = char_str[0:12]
    new_password = ensure_password_contains_special_char(password, max_acceptable_decimal)
    final_password = substitute_chars(new_password)

    return final_password


