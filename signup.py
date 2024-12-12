import customtkinter as ctk
from tkinter import messagebox

def signUp():
    ctk.set_appearance_mode("System")  
    ctk.set_default_color_theme("green")  

    root = ctk.CTk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 925
    window_height = 500

    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    root.title('Sign Up')
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    root.resizable(False, False)
    root.config(bg='#add123')

    frame = ctk.CTkFrame(root, width=500, bg_color='#add123', fg_color='#add123')  
    frame.pack(pady=(50, 0), padx=(20, 20))  

    heading = ctk.CTkLabel(frame, text='Sign Up', fg_color='transparent', font=('Microsoft YaHei UI Light', 23, 'bold'), text_color='#5A6C57')
    heading.pack(pady=(20, 10))

  
    user_entry = ctk.CTkEntry(frame, placeholder_text='Username', width=300, fg_color="white", text_color="black") 
    user_entry.pack(pady=(10, 10))

  
    email_entry = ctk.CTkEntry(frame, placeholder_text='Email', width=300, fg_color="white", text_color="black") 
    email_entry.pack(pady=(10, 10))

    
    password_entry = ctk.CTkEntry(frame, placeholder_text='Password', width=300, show='*', fg_color="white", text_color="black") 
    password_entry.pack(pady=(10, 10))

    
    confirm_password_entry = ctk.CTkEntry(frame, placeholder_text='Confirm Password', width=300, show='*', fg_color="white", text_color="black") 
    confirm_password_entry.pack(pady=(10, 10))


    sign_up_button = ctk.CTkButton(frame, text='Sign Up', fg_color='#525B44', border_color='#D3F1DF', hover_color="#85A98F", width=250)
    sign_up_button.pack(pady=(20, 10))

  
    label = ctk.CTkLabel(frame, text="Already have an account? Sign In", fg_color='transparent', font=('Microsoft YaHei UI Light', 9))
    label.pack(pady=(10, 0))

    signin_button = ctk.CTkButton(frame, text='Sign In', fg_color='#525B44', border_color='#D3F1DF', hover_color="#85A98F", command=root.destroy, width=250)
    signin_button.pack(pady=(0, 20))

    root.mainloop()


