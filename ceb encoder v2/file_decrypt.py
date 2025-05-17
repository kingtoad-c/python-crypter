from crypt import *
import os

encfile = input("Encrypted file name: ")
print("--------")
key = input("Key: ")
print("--------")
mult = input("Multiplier: ")
print("--------")
ext = input("Output (decrypted) file name: ")

shift = autocrack(key, int(mult))

with open(encfile, "r", encoding="utf-8") as encrypt:
    read_enc = str(encrypt.read())

decrypted_file = decrypt(read_enc, shift)

with open(ext, "w", encoding="utf-8") as new_file:
    new_file.write(decrypted_file)

print("done")
input("Press Enter to exit...")
