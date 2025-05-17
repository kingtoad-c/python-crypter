from crypt import *

text = input("Text to encrypt: ")

encrypted_key, multiplier = generate_key()
shift_value = autocrack(encrypted_key,multiplier)
encrypted_text = encrypt(text, shift_value)

print("-------------------------------------")
print(f"Encrypted text : {encrypted_text}")
print("-------------------------------------")
print(f"Encryption key : {encrypted_key.decode('utf-8')}")
print("-------------------------------------")
print(f"Encryption multiplier : {multiplier}")
print("-------------------------------------")

decrypted_text = decrypt(encrypted_text, shift_value)
print("Decrypted: ", decrypted_text)
input("press enter to exit...")