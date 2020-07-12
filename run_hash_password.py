#!/usr/bin/python3.8

import hash_password
import sys

general = sys.argv[1]
salt = sys.argv[2]

password = hash_password.SHA256_hash(general,salt)

print(password)
