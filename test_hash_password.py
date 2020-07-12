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

if __name__ == '__main__':
    unittest.main()
