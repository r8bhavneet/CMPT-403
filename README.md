# CMPT 403 - Security and Cryptography Assignments

This repository contains solutions for three assignments focused on security vulnerabilities and cryptographic challenges, specifically addressing buffer overflow exploits, breaking weak ciphers, and performing a padding oracle attack.

## Table of Contents
- [Buffer Overflow Vulnerabilities](#buffer-overflow-vulnerabilities)
- [Padding Oracle Attack](#padding-oracle-attack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Files Included](#files-included)

## Buffer Overflow Vulnerabilities

### Description
This assignment involves exploiting buffer overflow vulnerabilities in a C++ program (`login.cpp`) that checks user credentials in three different ways. The program interacts with a `password.txt` file, which is used to validate the user's login. The goal is to bypass these checks and achieve a successful login using different buffer overflow techniques.

### Task Breakdown
1. **Method 1:** `./login-i <username> <password>`
   - Exploit a simple buffer overflow to achieve a successful login.
   - Submit your username and password in `a1a.txt`.

2. **Method 2:** `./login-j <username> <password>`
   - Exploit a buffer overflow with a hardcoded canary.
   - Submit your username and password in `a1b.txt`.

3. **Method 3:** `./login-k <username> <password>`
   - Exploit a buffer overflow where the canary is randomized.
   - Submit your username and password in `a1c.txt`.

### Files
- `login.cpp`: The C++ source code with the vulnerabilities.
- `password.txt`: Provided for testing, but not used in the final submission.
- `a1a.txt`, `a1b.txt`, `a1c.txt`: Files containing the successful username and password combinations.


## Padding Oracle Attack

### Description
This assignment focuses on exploiting a padding oracle vulnerability in AES encryption using CBC mode. You will develop a program that automates the decryption process by interacting with a padding oracle, eventually recovering the entire plaintext.

### Steps
1. **Decrypt Byte:** Recover the last byte of the final block.
2. **Decrypt Block:** Recover the entire final block.
3. **Decrypt:** Decrypt all blocks of the ciphertext.

### Files
- `decrypt.py`: Python script that performs the decryption using the padding oracle.
- `ciphertext`: Input ciphertext file for the decryption process.
- `plaintext.txt`: Output file containing the recovered plaintext.

## Setup Instructions

### Prerequisites
- C++ compiler (for compiling `login.cpp`)
- Python 3 (for running `decrypt.py`)
- Linux or macOS environment (for running the assignments as intended)

### Compilation
To compile the C++ code, use the following command:
```bash
g++ -o login login.cpp
```

## Usage

### Description
Buffer Overflow
To run the buffer overflow exploits:

```bash
./login-i $(sed -n '1p' a1a.txt) $(sed -n '2p' a1a.txt)
./login-j $(sed -n '1p' a1b.txt) $(sed -n '2p' a1b.txt)
./login-k $(sed -n '1p' a1c.txt) $(sed -n '2p' a1c.txt)
```

