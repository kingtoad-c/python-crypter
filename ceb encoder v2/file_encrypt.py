from crypt import *
import os


key,mult = generate_key()
shift = autocrack(key,mult)

file = input("file name:")

f = open(file)

encrypted_file = encrypt(f.read(),shift)
encrypted_txt = str(encrypted_file)

os.system("echo > encrypted_file.ceb")
new_file = open("encrypted_file.ceb","w")

print("----------------")
print(f"|key: {key.decode('utf-8')}")
print(f"|mult: {mult}")
print("----------------")


new_file.write(encrypted_txt)
input("press enter to exit...")

