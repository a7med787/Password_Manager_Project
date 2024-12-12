from cryptography.fernet import Fernet
from DataStructure import StackList
from DataStructure import BinarySearchTree
import os

Storage1 = StackList()
Storage2 = BinarySearchTree()

# Generate the key only if it doesn't already exist


def write_key():
    if not os.path.exists("Key.key"):
        key = Fernet.generate_key()
        with open("Key.key", "wb") as key_file:
            key_file.write(key)


write_key()

# Read the key from the file


def read_key():
    with open("Key.key", "rb") as file:
        key = file.read()
    return key


key = read_key()
fr = Fernet(key)

# Function to add a password entry


def add():
    name = input("Account username: ").strip()
    Website = input("Website: ").strip()
    password = input("Password: ").strip()

    encrypted_password = fr.encrypt(password.encode()).decode()

    with open("password.txt", "a") as f:
        f.write(f"{name}|{Website}|{encrypted_password}\n")
    print("Password added successfully!")

# Function to view stored password entries


def view():
    if not os.path.exists("password.txt") or os.stat("password.txt").st_size == 0:
        print("No passwords stored yet!")
        return

    with open("password.txt", "r") as f:
        for line in f:
            try:
                data = line.rstrip()
                name, Website, password = data.split("|")
                decrypted_password = fr.decrypt(password.encode()).decode()
                Storage1.add(name, decrypted_password, Website)
                Storage2.Add_To_Bst(name, decrypted_password, Website)
                Storage1.view()

            except Exception as e:
                print(f"Error decrypting line: {line}. Error: {e}")


# Main application loop
while True:
    mode = input(
        "Would you like to add or view passwords? Press 'q' to quit: ").strip().lower()

    match mode:
        case "q":
            print("Exiting the app. Goodbye!")
            break
        case "add":
            add()
        case "view":
            view()
        case _:
            print("Invalid option! Please choose 'add', 'view', or 'q'.")
