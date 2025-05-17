from crypt import *

print("------------------------------------------")
enctxt = input("input encrypted text to decrypt:")
print("==========================================")
key = input("input encrypted key:")
print("==========================================")
mult = input("input encrypted multiplier:")

shift = autocrack(key,mult)

detxt = decrypt(enctxt,shift)
print("==========================================")
print(f"decrypted text:{detxt}")
input("press enter to exit...")