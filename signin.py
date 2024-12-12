import customtkinter as ctk
from tkinter import messagebox


def signIn(): 
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


    frame = ctk.CTkFrame(root, width=500 , bg_color='#add123', fg_color='#add123')  
    frame.pack(pady=(100, 0), padx=(20, 0))  


    heading = ctk.CTkLabel(frame, text='Sign in',  fg_color='transparent', font=('Microsoft YaHei UI Light', 23, 
                                                                                        'bold') , text_color= '#5A6C57')
    heading.pack(pady=(20, 10))


    user_entry = ctk.CTkEntry(frame, placeholder_text='Username', width=250, fg_color="white", text_color="black") 
    user_entry.pack(pady=(10, 10))


    password_entry = ctk.CTkEntry(frame, placeholder_text='Password', width=250, show='*', fg_color="white", text_color="black") 
    password_entry.pack(pady=(10, 20))


    signin_button = ctk.CTkButton(frame, text='Sign in', width=250 , fg_color='#525B44' , border_color='#D3F1DF',hover_color="#85A98F" )
    signin_button.pack(pady=(10, 10))


    label = ctk.CTkLabel(frame, text="Don't have an account?", fg_color='transparent', font=('Microsoft YaHei UI Light', 9))
    label.pack(pady=(10, 0))

    sign_up_button = ctk.CTkButton(frame, text='Sign up', fg_color='#525B44',border_color='#D3F1DF', hover_color="#85A98F", width=20)
    sign_up_button.pack(pady=(0, 20))


    root.mainloop()