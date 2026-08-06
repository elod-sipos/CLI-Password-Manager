# CLI Password Manager

## Installation & Usage
```bash
git clone https://github.com/elod-sipos/CLI-Password-Manager.git
cd CLI-Password-Manager
pip install -r requirements.txt
```

```bash
python src/main.py
```

## About
A command-line password manager that encrypts saved passwords locally using AES-GCM, with the encryption key derived from a master password via Argon2id.

## Features
- Master password unlocks the vault (never stored)
- Passwords encrypted at rest with AES-GCM (random nonce per entry)
- Optional built-in password generator
- Vault stored as a local JSON file `~/.vault.json`