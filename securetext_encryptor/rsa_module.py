from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(plaintext, public_key_data):
    key = RSA.import_key(public_key_data)
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(plaintext.encode())

def rsa_decrypt(ciphertext, private_key_data):
    key = RSA.import_key(private_key_data)
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(ciphertext).decode()
