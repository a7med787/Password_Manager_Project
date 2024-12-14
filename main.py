import customtkinter as ctk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os
from app import openprogram

# Generate or read encryption key
def write_key():
    if not os.path.exists("Key.key"):
        key = Fernet.generate_key()
        with open("Key.key", "wb") as key_file:
            key_file.write(key)

write_key()

def read_key():
    with open("Key.key", "rb") as file:
        return file.read()

key = read_key()
fr = Fernet(key)

# Save user data to file
def save_user(username, email, password):
    encrypted_password = fr.encrypt(password.encode()).decode()
    with open("users.txt", "a") as file:
        file.write(f"{username}|{email}|{encrypted_password}\n")

# Check user credentials
def validate_user(username, password):
    if not os.path.exists("users.txt"):
        return False

    with open("users.txt", "r") as file:
        for line in file:
            stored_username, _, stored_encrypted_password = line.strip().split("|")
            if username == stored_username:
                decrypted_password = fr.decrypt(stored_encrypted_password.encode()).decode()
                return decrypted_password == password

    return False

# Open Password Manager
def open_password_manager(username):
    openprogram(username)

# Sign In Page
def signIn():
    def handle_sign_in():
        username = user_entry.get()
        password = password_entry.get()

        if validate_user(username, password):
            root.destroy()
            open_password_manager(username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def go_to_sign_up():
        root.destroy()
        signUp()

    root = ctk.CTk()
    root.title("Sign In")
    root.geometry(f"925x500+{(root.winfo_screenwidth() - 925)//2}+{(root.winfo_screenheight() - 500)//2}")
    root.resizable(False, False)
    root.config(bg='#add123')

    frame = ctk.CTkFrame(root, width=500, bg_color='#add123', fg_color='#add123')
    frame.pack(pady=(100, 0), padx=(20, 0))

    heading = ctk.CTkLabel(frame, text='Sign In', fg_color='transparent', font=('Microsoft YaHei UI Light', 23, 'bold'),
                           text_color='#5A6C57')
    heading.pack(pady=(20, 10))

    user_entry = ctk.CTkEntry(frame, placeholder_text='Username', width=250, fg_color="white", text_color="black")
    user_entry.pack(pady=(10, 10))

    password_entry = ctk.CTkEntry(frame, placeholder_text='Password', width=250, show='*', fg_color="white",
                                  text_color="black")
    password_entry.pack(pady=(10, 20))

    signin_button = ctk.CTkButton(frame, text='Sign In', width=250, fg_color='#525B44', border_color='#D3F1DF',
                                  hover_color="#85A98F", command=handle_sign_in)
    signin_button.pack(pady=(10, 10))

    label = ctk.CTkLabel(frame, text="Don't have an account?", fg_color='transparent',
                         font=('Microsoft YaHei UI Light', 9))
    label.pack(pady=(10, 0))

    sign_up_button = ctk.CTkButton(frame, text='Sign Up', fg_color='#525B44', border_color='#D3F1DF',
                                   hover_color="#85A98F", width=250, command=go_to_sign_up)
    sign_up_button.pack(pady=(0, 20))

    root.mainloop()

# Sign Up Page
def signUp():
    def handle_sign_up():
        username = user_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not username or not email or not password or not confirm_password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        save_user(username, email, password)
        messagebox.showinfo("Success", "Account created successfully!")
        root.destroy()
        signIn()

    def go_to_sign_in():
        root.destroy()
        signIn()

    root = ctk.CTk()
    root.title("Sign Up")
    root.geometry(f"925x500+{(root.winfo_screenwidth() - 925)//2}+{(root.winfo_screenheight() - 500)//2}")
    root.resizable(False, False)
    root.config(bg='#add123')

    frame = ctk.CTkFrame(root, width=500, bg_color='#add123', fg_color='#add123')
    frame.pack(pady=(50, 0), padx=(20, 20))

    heading = ctk.CTkLabel(frame, text='Sign Up', fg_color='transparent', font=('Microsoft YaHei UI Light', 23, 'bold'),
                           text_color='#5A6C57')
    heading.pack(pady=(20, 10))

    user_entry = ctk.CTkEntry(frame, placeholder_text='Username', width=300, fg_color="white", text_color="black")
    user_entry.pack(pady=(10, 10))

    email_entry = ctk.CTkEntry(frame, placeholder_text='Email', width=300, fg_color="white", text_color="black")
    email_entry.pack(pady=(10, 10))

    password_entry = ctk.CTkEntry(frame, placeholder_text='Password', width=300, show='*', fg_color="white",
                                  text_color="black")
    password_entry.pack(pady=(10, 10))

    confirm_password_entry = ctk.CTkEntry(frame, placeholder_text='Confirm Password', width=300, show='*',
                                          fg_color="white", text_color="black")
    confirm_password_entry.pack(pady=(10, 10))

    sign_up_button = ctk.CTkButton(frame, text='Sign Up', fg_color='#525B44', border_color='#D3F1DF',
                                   hover_color="#85A98F", width=250, command=handle_sign_up)
    sign_up_button.pack(pady=(20, 10))

    label = ctk.CTkLabel(frame, text="Already have an account? Sign In", fg_color='transparent',
                         font=('Microsoft YaHei UI Light', 9))
    label.pack(pady=(10, 0))

    signin_button = ctk.CTkButton(frame, text='Sign In', fg_color='#525B44', border_color='#D3F1DF',
                                  hover_color="#85A98F", command=go_to_sign_in, width=250)
    signin_button.pack(pady=(0, 20))

    root.mainloop()

# Start the app
signUp()