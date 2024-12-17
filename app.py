import tkinter as c
import customtkinter as ctk
from tkinter import messagebox
from cryptography.fernet import Fernet
from DataStructure import BinarySearchTree
import os

def openprogram(username):
    class StackList:
        def __init__(self):
            self.stack = []

        def add(self, username, password, website):
            self.stack.append((username, password, website))

        def deleteNode(self, username, website):
            for i, (name, pw, site) in enumerate(self.stack):
                if name == username and site == website:
                    del self.stack[i]
                    return True
            return False

        def is_empty(self):
            return len(self.stack) == 0

        def get_all(self):
            return reversed(self.stack)

        def search(self, username):
            return list(reversed([item for item in self.stack if item[0] == username]))


    Storage1 = StackList()
    Storage2 = BinarySearchTree()

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

    def load_passwords_from_file():
        if os.path.exists(f"{username}_password.txt"):
            with open(f"{username}_password.txt", "r")as f:
                lines = f.readlines()
                for line in reversed(lines):  # Reverse order to maintain LIFO
                    name, website, encrypted_password = line.strip().split("|")
                    Storage1.add(name, encrypted_password, website)


    def refresh_passwords(frame):
        for widget in frame.winfo_children():
            widget.destroy()

        canvas = c.Canvas(frame, bg='#add123')
        scrollbar = c.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = c.Frame(canvas, bg='#add123')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        if Storage1.is_empty():
            c.Label(scrollable_frame, text="No passwords stored yet!",
                    bg='#add123', fg='white', font=('Arial', 12)).pack()
            return

        for item in Storage1.get_all():
            name, encrypted_password, website = item
            try:
                decrypted_password = fr.decrypt(
                    encrypted_password.encode()).decode()
                entry = c.Frame(scrollable_frame, bg='#add123', pady=5)
                entry.pack(fill="x", padx=10, pady=5)

                c.Label(entry, text=f"Username: {name}", bg='#add123', fg='blue', font=(
                    'Arial', 12)).pack(side="left")
                c.Label(entry, text=f"Website: {website}", bg='#add123', fg='green', font=(
                    'Arial', 12)).pack(side="left", padx=10)
                c.Label(entry, text=f"Password: {decrypted_password}", bg='#add123', fg='red', font=(
                    'Arial', 12)).pack(side="left", padx=10)

                delete_button = ctk.CTkButton(entry, text="Delete", fg_color='#FF4B4B', text_color="white",
                                            command=lambda n=name, w=website: delete_password(n, w))
                delete_button.pack(side="right")
            except Exception as e:
                print(f"Error decrypting password: {e}")

    #

    def delete_password(name, website):
        deleted = Storage1.deleteNode(name, website)

        if deleted:
            updated_lines = []
            file_path = f"{username}_password.txt"
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    for line in f:
                        try:
                            file_name, file_website, _ = line.strip().split("|")
                            # Keep lines that don't match the entry to delete
                            if file_name != name or file_website != website:
                                updated_lines.append(line)
                        except ValueError:
                            continue  # Skip malformed lines

                # Overwrite the file with updated data
                with open(file_path, "w") as f:
                    f.writelines(updated_lines)

            messagebox.showinfo("Success", "Password deleted successfully!")
            refresh_passwords(password_frame)
        else:
            messagebox.showinfo("Not Found", "No matching entry found.")



    def add_page():
        new_window = ctk.CTkToplevel()
        new_window.title("Add New Password")
        new_window.geometry(f"400x300+{(925-400)//2}+{(500-300)//2}")
        new_window.config(bg='#E1FFBB')

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        username_label = ctk.CTkLabel(
            new_window, text="Username:", bg_color='#E1FFBB')
        website_label = ctk.CTkLabel(
            new_window, text="Website:", bg_color='#E1FFBB')
        password_label = ctk.CTkLabel(
            new_window, text="Password:", bg_color='#E1FFBB')

        username_entry = ctk.CTkEntry(new_window, placeholder_text="Username")
        website_entry = ctk.CTkEntry(new_window, placeholder_text="Website")
        password_entry = ctk.CTkEntry(
            new_window, show="*", placeholder_text="Password")

        def add_password():
            name = username_entry.get()
            website = website_entry.get()
            password = password_entry.get()

            if not name or not website or not password:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            encrypted_password = fr.encrypt(password.encode()).decode()

            with open(f"{username}_password.txt", "a") as f:
                f.write(f"{name}|{website}|{encrypted_password}\n")

            Storage1.add(name, encrypted_password, website)
            Storage2.Add_To_Bst(name, encrypted_password, website)
            messagebox.showinfo("Success", "Password added successfully!")
            refresh_passwords(password_frame)

        add_button = ctk.CTkButton(
            new_window, text="Add Password", command=add_password)

        username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        website_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        website_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        add_button.grid(row=3, columnspan=2, pady=20)


    def search_password():
        query = search_entry.get()

        if not query:
            messagebox.showerror("Error", "Please enter a username to search.")
            return

        results = Storage1.search(query)

        if results:
            result_window = ctk.CTkToplevel()
            result_window.title("Search Results")
            result_window.geometry(f"400x300+{(925-400)//2}+{(500-300)//2}")
            result_window.config(bg='#E1FFBB')

            for name, encrypted_password, website in results:
                try:
                    decrypted_password = fr.decrypt(
                        encrypted_password.encode()).decode()
                    c.Label(result_window, text=f"Username: {name}, Website: {website}, Password: {decrypted_password}",
                            bg='#E1FFBB', fg='black', font=('Arial', 12)).pack(anchor="w", padx=10, pady=5)
                except Exception as e:
                    print(f"Error decrypting password: {e}")
        else:
            messagebox.showinfo("Not Found", "No matching username found.")


    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    App_Window = ctk.CTk()
    App_Window.title('Password Manager')
    App_Window.geometry(f"925x500+{(App_Window.winfo_screenwidth() - 925)//2}+{(App_Window.winfo_screenheight() - 500)//2}")
    App_Window.resizable(False, False)
    App_Window.config(bg='#add123')


    Programe_titleLabel = ctk.CTkLabel(App_Window, text="Password Manager",
                                    font=('Microsoft YaHei UI Light', 30, 'bold'),
                                    text_color="#5A6C57", bg_color='#add123')
    Programe_titleLabel.place(x=20, y=20)

    add_button = ctk.CTkButton(App_Window, text="Add New", command=add_page, width=100, fg_color='#525B44',
                            bg_color="#add123", border_color='#D3F1DF', hover_color="#85A98F",
                            text_color="#D3F1DF", font=('Microsoft YaHei UI Light', 15, 'bold'),
                            corner_radius=10)
    add_button.place(y=80, x=20)

    search_entry = ctk.CTkEntry(App_Window, placeholder_text="Search for a username", width=300, fg_color="white",
                                bg_color="#add123", text_color="black")
    search_entry.place(y=80, x=150)

    search_button = ctk.CTkButton(
        App_Window, text="Search", width=50, bg_color="#add123", command=search_password)
    search_button.place(y=80, x=460)

    password_frame = c.Frame(App_Window, bg='#add123')
    password_frame.place(x=20, y=130, width=880, height=330)

    # Load passwords from file at startup
    load_passwords_from_file()
    refresh_passwords(password_frame)

    App_Window.mainloop()
