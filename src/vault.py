import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT_FILE = "test.json"

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
        json.dump(data, file, indent=5)

# Adds new entry
def add_entry(service, password):
    vault = load_vault()
    vault[service.lower()] = {
        "password": password
    }
    save_vault(vault)

# Retrieves entry
def get_entry(service):
    vault = load_vault()
    return vault.get(service.lower())
