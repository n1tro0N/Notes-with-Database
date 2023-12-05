import customtkinter as ctk
from customtkinter import CTkLabel, CTkEntry, CTkButton
root = ctk.CTk()
ctk.set_appearance_mode('dark')
root.title("Registration Form")
root.geometry("600x600")

name = CTkLabel(root, text="Name")
surname = CTkLabel(root, text="Surname")
contact = CTkLabel(root, text="Contact")
email = CTkLabel(root, text="Email")

name.grid(row=1, column=0)
surname.grid(row=2, column=0)
contact.grid(row=3, column=0)
email.grid(row=4, column=0)


name_field = CTkEntry(root)
surname_field = CTkEntry(root)
contact_field = CTkEntry(root)
email_field = CTkEntry(root)


name_field.grid(row=1, column=1, ipadx="100")
surname_field.grid(row=2, column=1, ipadx="100")
contact_field.grid(row=3, column=1, ipadx="100")
email_field.grid(row=4, column=1, ipadx="100")


submit = CTkButton(root, text="Submit")
submit.grid(row=5, column=1)

root.mainloop()
