import base64
import time
import datetime
from aes_module import aes_encrypt, aes_decrypt
from des_module import des_encrypt, des_decrypt
from rsa_module import rsa_encrypt, rsa_decrypt, generate_keys

def log_error(algorithm, error_msg):
    with open("error_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] [{algorithm}] ERROR: {error_msg}\n")

def print_banner():
    print("=" * 80)
    print("🛡️  SECURETEXT ENCRYPTOR - Multi-Algorithm Text Encryption Tool")
    print("=" * 80)

def print_header(title):
    print("\n" + "─" * 80)
    print(f"🔒 {title}")
    print("─" * 80)

def print_result(original, encoded, decrypted):
    print(f"📝 Original Message  : {original}")
    print(f"📦 Encrypted (Base64): {encoded}")
    print(f"🔓 Decrypted Message : {decrypted}")
    print("✅ Process completed successfully.\n")

def encrypt_decrypt_aes(message):
    print_header("AES (Advanced Encryption Standard)")
    key = b'ThisIsA16ByteKey'  # 128-bit key
    print(f"🔑 AES Key (128-bit) : {key.decode()}")
    try:
        encrypted = aes_encrypt(message, key)
        encoded = base64.b64encode(encrypted).decode()
        decrypted = aes_decrypt(encrypted, key).decode()
        print_result(message, encoded, decrypted)
    except Exception as e:
        print(f"❌ AES Error: {e}")
        log_error("AES", str(e))

def encrypt_decrypt_des(message):
    print_header("DES (Data Encryption Standard)")
    key = b'8bytekey'  # 64-bit key
    print(f"🔑 DES Key (64-bit)  : {key.decode()}")
    try:
        encrypted = des_encrypt(message, key)
        encoded = base64.b64encode(encrypted).decode()
        decrypted = des_decrypt(encrypted, key)
        print_result(message, encoded, decrypted)
    except Exception as e:
        print(f"❌ DES Error: {e}")
        log_error("DES", str(e))

def encrypt_decrypt_rsa(message):
    print_header("RSA (Public-Key Cryptography)")
    try:
        private_key, public_key = generate_keys()
        print("🔑 Generated 2048-bit RSA Key Pair")
        encrypted = rsa_encrypt(message, public_key)
        encoded = base64.b64encode(encrypted).decode()
        decrypted = rsa_decrypt(encoded, private_key)
        print_result(message, encoded, decrypted)
    except Exception as e:
        print(f"❌ RSA Error: {e}")
        log_error("RSA", str(e))

def main():
    while True:
        print_banner()
        message = input("📥 Enter the message you want to encrypt: ").strip()

        if not message:
            print("⚠️  Message cannot be empty. Please try again.\n")
            continue

        print("\n🔽 Select an Encryption Algorithm:")
        print("  1️⃣  AES  - Fast, secure symmetric encryption (128-bit)")
        print("  2️⃣  DES  - Older symmetric encryption (64-bit)")
        print("  3️⃣  RSA  - Asymmetric encryption with key pairs (2048-bit)")

        choice = input("\n🔢 Your choice (1 / 2 / 3): ").strip()

        print("\n⏳ Processing your request...\n")
        time.sleep(1.2)

        if choice == '1':
            encrypt_decrypt_aes(message)
        elif choice == '2':
            encrypt_decrypt_des(message)
        elif choice == '3':
            encrypt_decrypt_rsa(message)
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.\n")
            continue

        again = input("🔁 Do you want to try another message? (y/n): ").strip().lower()
        if again != 'y':
            break

    print("\n🎉 Thank you for using SecureText Encryptor. Stay safe and secure!")
    print("=" * 80)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⛔ Interrupted by user. Exiting securely.")
    except Exception as e:
        print(f"\n🔥 Unexpected error occurred: {e}")
        log_error("MAIN", str(e))
