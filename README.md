# 🔐 Ceb cypher

A Python-based encryption tool that combines multiple layers of **Base64 encoding** and **Caesar cipher shifts** using two encryption keys for enhanced data obfuscation. Perfect for educational purposes, CTF challenges, or lightweight data masking.

## 🚀 Features

- 🔐 Two encryption keys controlling:
  - Number of **Base64 encoding layers** (1–10,000)
  - **Caesar cipher** encrypted shift value (1–10,000)
- 🔁 Multi-layer Base64 encoding and decoding
- 🔁 Multi-round Caesar cipher encryption and decryption
- 🔄 Supports both **encryption** and **decryption**
- 🧪 Simple CLI interface

## 🧠 How It Works

1. **Encryption**:
   - The first key sets how many times the input is Base64 encoded.
   - The second key sets the Caesar cipher shift value (or number of rounds).
   - The Caesar cipher is applied using the shift key.
   - Then Base64 encoding is applied repeatedly according to the first key.

2. **Decryption**:
   - Base64 decoding is applied repeatedly according to the first key.
   - Caesar cipher is reversed using the second key.

> ⚠️ This tool is for **educational and obfuscation purposes only**. It is **not cryptographically secure** and should not be used for protecting sensitive information in production.

## 🧑‍💻 Author

**kingtoad-c**  
[GitHub](https://github.com/kingtoad-c)

## 📜 License

This project is licensed under the MIT License.
