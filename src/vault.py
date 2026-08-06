import json
import os
from crypto import encrypt, decrypt
from crypto import encrypt, decrypt, generate_salt

VAULT_FILE = os.path.expanduser("~/.vault.json")

# Read vault file and return as dictionary
def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    
    with open(VAULT_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

# Updates dictionary
def save_vault(data):
    with open(VAULT_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Adds new entry
def add_entry(service, password, key):
    vault = load_vault()
    nonce, ciphertext = encrypt(key, password)

    vault[service.lower()] = {
        "nonce": nonce.hex(),
        "ciphertext": ciphertext.hex()
    }
    save_vault(vault)

# Retrieves entry
def get_entry(service, key):
    vault = load_vault()
    entry = vault.get(service.lower())

    if entry is None:
        return None

    nonce = bytes.fromhex(entry["nonce"])
    ciphertext = bytes.fromhex(entry["ciphertext"])
    return decrypt(key, nonce, ciphertext)
    

def get_or_create_salt():
    vault = load_vault()
    
    if "_salt" in vault:
        return bytes.fromhex(vault["_salt"])

    salt = generate_salt()
    vault["_salt"] = salt.hex()
    save_vault(vault)
    return salt

