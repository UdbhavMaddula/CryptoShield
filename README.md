# 🛡️ CryptoShield

An interactive educational cryptography platform built using **Python, Streamlit, and PyCryptodome** to demonstrate how modern encryption algorithms work.

CryptoShield helps users understand the difference between **symmetric** and **asymmetric** cryptography by allowing them to encrypt and decrypt text using industry-relevant algorithms through an intuitive web interface.

---

## 🚀 Features

### 🔐 AES-256 Encryption (Recommended)
- AES-256 CBC Mode Encryption
- AES-256 CBC Mode Decryption
- Random Initialization Vector (IV)
- PKCS7 Padding
- SHA-256 Key Derivation
- Wrong Key Detection
- Educational Insights

### ⚠️ DES Encryption (Legacy)
- DES CBC Mode Encryption
- DES CBC Mode Decryption
- Random Initialization Vector (IV)
- Educational Warning about DES vulnerabilities
- Historical significance of DES

### 🔑 RSA Encryption (Asymmetric Cryptography)
- RSA 2048-bit Key Pair Generation
- Public Key Encryption
- Private Key Decryption
- OAEP Padding (Modern RSA Standard)
- Session-Based Key Persistence
- Automatic Key Autofill
- Educational Insights

---

## 📚 Educational Objectives

CryptoShield is designed to help learners understand:

- Symmetric Encryption
- Asymmetric Encryption
- AES (Advanced Encryption Standard)
- DES (Data Encryption Standard)
- RSA Cryptography
- CBC Mode Operation
- Initialization Vectors (IVs)
- OAEP Padding
- Base64 Encoding
- Cryptographic Error Handling
- Real-World Applications of Encryption

---

## 🛠️ Technologies Used

- Python
- Streamlit
- PyCryptodome
- Hashlib
- Base64

---

## 🏗️ Project Structure

```
CryptoShield/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/UdbhavMaddula/CryptoShield.git
cd CryptoShield
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 How It Works

### AES / DES Workflow

```
Plaintext
    ↓
Secret Key
    ↓
Encryption
    ↓
Ciphertext
    ↓
Decryption
    ↓
Recovered Plaintext
```

### RSA Workflow

```
Generate RSA Key Pair
        ↓
Public Key → Encrypt
        ↓
Ciphertext
        ↓
Private Key → Decrypt
        ↓
Recovered Plaintext
```

---

## 🌍 Real-World Applications

### AES
- WhatsApp
- VPNs
- Banking Systems
- BitLocker
- Enterprise Security Solutions

### RSA
- HTTPS
- SSL/TLS Certificates
- Secure Email
- Digital Certificates
- Key Exchange Protocols

### DES
- Historical Banking Systems
- Early Government Standards
- Cryptography Education

---

## ⚠️ Disclaimer

This project was developed for **educational purposes** to demonstrate cryptographic concepts.

- AES-256 is considered secure for modern applications.
- RSA-2048 is widely used in secure communications.
- DES is included to illustrate the evolution of cryptography and should **not** be used in production environments.

---

## 🔮 Future Improvements

Potential enhancements for future versions include:

- Digital Signatures using RSA
- File Encryption and Decryption
- Drag-and-Drop File Support
- Hashing Demonstrations (SHA Family)
- Additional Educational Visualizations
- Improved UI Enhancements

---

## 👨‍💻 Developed By

**Udbhav (Maanas Sri Udbhav Maddula)**

Cybersecurity Enthusiast | Chess Player | Aspiring Security Professional

---

## ⭐ Support the Project

If you found CryptoShield useful or educational, consider giving this repository a **star** to support the project and future improvements.
