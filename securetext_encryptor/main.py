import base64
from aes_module import aes_encrypt, aes_decrypt
from des_module import des_encrypt, des_decrypt
from rsa_module import rsa_encrypt, rsa_decrypt, generate_keys

def main():
    print("Choose encryption type: AES, DES, RSA")
    algo = input("Enter algorithm: ").strip().upper()
    plaintext = input("Enter text to encrypt: ")

    if algo == 'AES':
        key = b'1234567890abcdef'  # 16-byte key
        ciphertext = aes_encrypt(plaintext, key)
        print("Encrypted:", base64.b64encode(ciphertext))
        decrypted = aes_decrypt(ciphertext, key)
        print("Decrypted:", decrypted.decode())

    elif algo == 'DES':
        key = b'8bytekey'  # 8-byte key
        ciphertext = des_encrypt(plaintext, key)
        print("Encrypted:", base64.b64encode(ciphertext))
        decrypted = des_decrypt(ciphertext, key)
        print("Decrypted:", decrypted)

    elif algo == 'RSA':
        private_key, public_key = generate_keys()
        ciphertext = rsa_encrypt(plaintext, public_key)
        print("Encrypted:", base64.b64encode(ciphertext))
        decrypted = rsa_decrypt(ciphertext, private_key)
        print("Decrypted:", decrypted)

    else:
        print("Unsupported algorithm!")

if __name__ == "__main__":
    main()
