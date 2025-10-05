import tkinter
from views.register_view import RegisterView
# from views.loginView import LoginView
# from models.users_model import UserModel
# from tkinter import ttk
# from tkinter import messagebox


class LoginView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Iniciar sesión")  # Fixed typo
        self.geometry("400x230")
        self.resizable(width=False, height=False)
        self.user_controller = user_controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Username section
        self.username_label = tkinter.Label(self, text="Usuario:")
        self.username_entry = tkinter.Entry(self)
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password section
        self.password_label = tkinter.Label(self, text="Contraseña:")
        self.password_entry = tkinter.Entry(self, show="*")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.login_button = tkinter.Button(self, text="Iniciar sesión", command=self._default_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=15)

        self.register_button = tkinter.Button(self, text="Registrarse", command=self._default_register)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

    def _default_login(self):
        print("Default login action - no callback set yet")

    def _default_register(self):
        self.user_controller.show_register_window()
        print("Default register action - no callback set yet")

    def on_login(self, callback):
        """Set the login button callback"""
        print("Setting login callback")
        self.login_button.config(command=callback)

    def on_register(self, callback):
        
        print("Setting register callback")
        self.register_button.config(command=callback)
    def get_credentials(self):
        """Helper method to get username and password"""
        return self.username_entry.get(), self.password_entry.get()

    def clear_entries(self):
        """Helper method to clear the entry fields"""
        self.username_entry.delete(0, tkinter.END)
        self.password_entry.delete(0, tkinter.END)
