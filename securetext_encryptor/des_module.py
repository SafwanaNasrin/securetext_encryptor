from Crypto.Cipher import DES
import os

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text.encode())
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).decode().rstrip()
    return plaintext
