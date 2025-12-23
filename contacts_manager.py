import json
import re
import csv
from datetime import datetime

def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    return (True, digits) if 10 <= len(digits) <= 15 else (False, None)

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def save_data(contacts, filename="contacts_data.json"):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)

def load_data(filename="contacts_data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def main():
    contacts = load_data()
    print("--- Contact Manager Loaded ---")
   

if __name__ == "__main__":
    main()