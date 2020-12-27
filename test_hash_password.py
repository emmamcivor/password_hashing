#!/usr/bin/python3
import unittest
import hash_password

## Test the mapping function

test_str = "Emma's Test!" # 69 109 109 97 39 115 32 84 69 115 116
test_bytes = b"Emma's Test!"
min_acceptable_decimal = 0
max_acceptable_decimal = 255

class test_output_characteristics_mapping(unittest.TestCase):           
# test 1: output is a str
    def test_output_str(self):
        char_str = hash_password.convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,test_bytes)
        self.assertIsInstance(char_str,str)

# test 2: character string is same length as hash
    def test_output_length(self):
        char_str = hash_password.convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,test_bytes)
        self.assertEqual(len(char_str),len(test_str))
        self.assertEqual(len(char_str),len(test_bytes))

# test 3: check output is correct. Pass in Emma's Test in btes form. Check output returns Emma's Test.
    def test_output_correct(self):
        char_str = hash_password.convert_bytes_char_str(min_acceptable_decimal,max_acceptable_decimal,test_bytes)
        for i in range(len(test_str)):
            self.assertEqual(char_str[i],test_str[i])

## Test the hashing password function
class test_output_characteristics_hashing(unittest.TestCase):           
    def test_type(self):
        # check the output is a string
        general = 'test'
        salt = 'one'
        password = hash_password.SHA256_hash(general,salt)
        self.assertIsInstance(password,str)

    def test_length(self):
        # check the output is of length 12
        general = 'test'
        salt = 'one'
        password = hash_password.SHA256_hash(general,salt)
        self.assertEqual(len(password),12)

## Test the character substitution
class test_char_sub(unittest.TestCase):           
    def test_sub(self):
        password = 'password[\]`'
        new_password = hash_password.substitute_chars(password)
        self.assertEqual(new_password,'password[\]*')

## Test function to identify special characters
class test_is_special_char(unittest.TestCase):           
    def test_symbols_1(self):
        output = hash_password.is_char_special('%')
        self.assertEqual(output,True)

    def test_symbols_2(self):
        output = hash_password.is_char_special('=')
        self.assertEqual(output,True)

    def test_symbols_3(self):
        output = hash_password.is_char_special('a')
        self.assertEqual(output,False)

    def test_symbols_4(self):
        output = hash_password.is_char_special('A')
        self.assertEqual(output,False)

## Test function to identify whether special character is in password
class test_password_special_char(unittest.TestCase):           
    def test_symbols_1(self):
        password = 'abAB'    
        output = hash_password.password_contains_special_char(password)
        self.assertEqual(output,False)

    def test_symbols_2(self):
        password = 'abAB123'    
        output = hash_password.password_contains_special_char(password)
        self.assertEqual(output,False)

    def test_symbols_3(self):
        password = 'abAB%='    
        output = hash_password.password_contains_special_char(password)
        self.assertEqual(output,True)

## Test function to update password to include a special character
class test_update_with_special_char(unittest.TestCase):           
    def test_pw_1(self):
        password = 'test5'
        max_acceptable_decimal = 122
        output = hash_password.update_password_special_character(password,max_acceptable_decimal)
        self.assertEqual(output,'test?')

    def test_pw_2(self):
        password = 'test7'
        max_acceptable_decimal = 122
        output = hash_password.update_password_special_character(password,max_acceptable_decimal)
        self.assertEqual(output,'test_')

    def test_pw_3(self):
        password = 'testq'
        max_acceptable_decimal = 122
        output = hash_password.update_password_special_character(password,max_acceptable_decimal)
        self.assertEqual(output,'test(')

    def test_pw_4(self):
        password = 'test('
        max_acceptable_decimal = 122
        output = hash_password.update_password_special_character(password,max_acceptable_decimal)
        self.assertEqual(output,'test(')

## Test function to update password to include a special character
class test_ensure_password_special_char(unittest.TestCase):           
    def test_pw_sc_1(self):
        password = 'test5'
        max_acceptable_decimal = 122
        output = hash_password.ensure_password_contains_special_char(password, max_acceptable_decimal)
        self.assertEqual(output,'test?')

    def test_pw_sc_2(self):
        password = 'test%'
        max_acceptable_decimal = 122
        output = hash_password.ensure_password_contains_special_char(password, max_acceptable_decimal)
        self.assertEqual(output,'test%')

if __name__ == '__main__':
    unittest.main()
