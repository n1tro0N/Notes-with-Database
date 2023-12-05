import customtkinter as ctk
from utils import hash_password
from database.crud import add_user
from tkinter.messagebox import showinfo, showwarning


class RegisterPage(ctk.CTkFrame):
    def __init__(self, container, user_id, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container

        label = ctk.CTkLabel(self, text="Register")
        label.pack(pady=20)

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=20, padx=40, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Modern Register System UI")
        label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(
            master=frame, placeholder_text="Password", show="*"
        )
        self.user_pass.pack(pady=12, padx=10)

        self.user_pass_repeat = ctk.CTkEntry(
            master=frame, placeholder_text="Repeat Password", show="*"
        )
        self.user_pass_repeat.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Register", command=self.register)
        button.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Sign In", command=self.move_to_login)
        button.pack(pady=12, padx=10)

    def move_to_login(self):
        self.container.show_default_page()

    def register(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        reapet_pass = self.user_pass_repeat.get()

        if username == '' or password == '':
            showwarning(title='Empty Fields!', message='Login and Passqord Required')
        elif reapet_pass != password:
            showwarning(
                "Passwords doesn't match"
                "Enter a different password"
            )
        else:
            hashed_password = hash_password(password)
            user = add_user(username, hashed_password)
            print('USER ID:', user)
            self.container.show_default_page()
            showinfo('Login Redirect', 'Account created!')
