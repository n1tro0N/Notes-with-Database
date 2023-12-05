import customtkinter as ctk

from database.crud import get_user, add_user
from tkinter.messagebox import showerror, showinfo, showwarning
from .notes import NotePage
from .register_page import RegisterPage
from  utils import hash_password


class LoginPage(ctk.CTkFrame):
    def __init__(self, container, user_id, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container

        label = ctk.CTkLabel(self, text="LOGIN")
        label.pack(pady=20)

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=20, padx=40, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Modern Login System UI")
        label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(
            master=frame, placeholder_text="Password", show="*"
        )
        self.user_pass.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Login", command=self.login)
        button.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Sign Up", command=self.move_to_register)
        button.pack(pady=12, padx=10)


    def login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()

        if username == '' or password == '':
            showwarning(title='Empty fields!', message='Login and Passqord Required')
        else:
            hashed_password = hash_password(password)
            user = get_user(username, hashed_password)
        if not user:
            showwarning('User not found', f'Incorrect username or password')
        else:
            self.container.show_page(NotePage, user.user_id)

    def move_to_register(self):
        self.container.show_page(RegisterPage)