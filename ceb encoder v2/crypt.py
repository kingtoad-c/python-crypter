import base64
import random

def generate_key():
    raw_key = random.randint(1, 10000)
    multiplier = random.randint(1, 10000)
    semi_encrypted_key = raw_key * multiplier
    bytes_key = str(semi_encrypted_key).encode("utf-8")
    encrypted_key = base64.b64encode(bytes_key)
    return encrypted_key, multiplier

def calculate_shift(key, mult):
    shift = int(key) / int(mult)
    shift_str = str(int(shift))
    shift_bytes = shift_str.encode("utf-8")
    encoded_bytes = base64.b64encode(shift_bytes)
    return encoded_bytes

def get_shift_from_b64(shift_b64):
    shift_bytes = base64.b64decode(shift_b64)
    shift_int = int(shift_bytes.decode("utf-8"))
    return shift_int

def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char
    encrypted_bytes = encrypted.encode("utf-8")
    encrypted_64 = base64.b64encode(encrypted_bytes)
    return encrypted_64.decode("utf-8")

def decrypt(text, shift):
    text_bytes = base64.b64decode(text)
    text_plain = text_bytes.decode("utf-8")
    text = str(text_plain)
    decrypted = ""
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted += char
    return decrypted

def autocrack(encrypted_key, multiplier):
    decoded_bytes = base64.b64decode(encrypted_key)
    original_key = decoded_bytes.decode("utf-8")
    shift_b64 = calculate_shift(int(original_key), multiplier)
    shift_value = get_shift_from_b64(shift_b64)
    return shift_value

