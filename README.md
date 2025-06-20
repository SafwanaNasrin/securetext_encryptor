# 🛡️ SecureText Encryptor – Multi-Algorithm Encryption Tool

A beginner-friendly yet powerful Python tool to **encrypt and decrypt messages** using **AES**, **DES**, or **RSA** algorithms. Built to demonstrate practical cryptographic concepts in a simple and interactive way.

---

## ✨ Key Features

- 🔒 **AES (Advanced Encryption Standard)** – Fast, secure symmetric encryption
- 🧱 **DES (Data Encryption Standard)** – Legacy symmetric encryption
- 🔐 **RSA (Public Key Encryption)** – Asymmetric encryption with 2048-bit key pair
- 📦 Output is Base64 encoded for easy readability
- 📝 Error logs saved in `error_log.txt`
- 🎨 Beautiful CLI with emoji support and structured sections

---

## 📸 Demo Output

🛡️ SECURETEXT ENCRYPTOR - Multi-Algorithm Text Encryption Tool
📥 Enter the message you want to encrypt: hello123

🔽 Select an Encryption Algorithm:
1️⃣ AES - Fast, secure symmetric encryption (128-bit)
2️⃣ DES - Older symmetric encryption (64-bit)
3️⃣ RSA - Asymmetric encryption with key pairs (2048-bit)

⏳ Processing your request...

🔒 AES (Advanced Encryption Standard)
🔑 AES Key (128-bit) : ThisIsA16ByteKey
📝 Original Message : hello123
📦 Encrypted (Base64): a4pS3oS4mkbT8XGHV9G7aA==
🔓 Decrypted Message : hello123
✅ Process completed successfully.


---

## 📁 Project Structure

securetext_encryptor/
├── securetext_main.py # Main CLI tool
├── aes_module.py # AES encrypt/decrypt logic
├── des_module.py # DES encrypt/decrypt logic
├── rsa_module.py # RSA encryption + key generation
├── error_log.txt # Logs any errors during encryption
└── README.md # This file


---

## 🧰 Dependencies

- Python 3.x
- [PyCryptodome](https://pypi.org/project/pycryptodome/)

Install using pip:

```bash
pip install pycryptodome

🚀 Getting Started

    Clone the repository:

git clone https://github.com/SafwanaNasrin/securetext_encryptor.git
cd securetext_encryptor

    Run the tool:

python test_all.py

    Follow the prompts to enter your message and choose an encryption algorithm.

🔐 Algorithms Explained
Algorithm	Type	Key Size	Usage
AES	Symmetric	128-bit	Fast, secure for general use
DES	Symmetric	64-bit	Historical encryption (for study)
RSA	Asymmetric	2048-bit keys	Secure key exchange, emails
🧑‍💻 Author

Safwana Nasrin
Cybersecurity Enthusiast | Python Developer
📫 LinkedIn (https://www.linkedin.com/in/SafwanaNasrin
🎓 B.Sc. in Computer Science | Passionate about data security
📜 License

This project is licensed under the MIT License – free to use, study, modify, and share.
🤝 Contribute

Pull requests are welcome! If you’d like to improve the tool or add more encryption methods, feel free to open an issue or submit changes.
🔖 Tags

#Encryption #Python #AES #RSA #DES #CyberSecurity #CLIApp #CryptoTool #SecureText

    🔐 Always encrypt responsibly. This tool is for learning purposes only.


---

Let me know if you want:
- Custom GitHub badges (e.g., Python version, License)
- A visual banner
- README in PDF format for portfolio use  
- README in **short resume-line format**

I can also help you make this project portfolio-ready for internships!

