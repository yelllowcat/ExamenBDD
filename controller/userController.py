import tkinter

from _curses import window
from views.loginView import LoginView
from views.register_view import RegisterView
from tkinter import messagebox

class UserController():
    def __init__(self, user_model):
        self.user_model = user_model
        self.login_view = None
        self.register_view = None

    def run(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def show_register_window(self):
        if self.register_view is None or not self.register_view.winfo.exxists():
            self.register_view = RegisterView(self)
        self.register_view.lift()

    def handle_register(self, username, firstname, lastname, password, window):
        if not all([username, firstname, lastname, password]):
            messagebox.showerror("Error", "Todos los campos son obligatorios!")
            return
        
        if self.user_model.create_user(username, firstname, lastname, password):
            messagebox.showinfo("Success", "User registered successfully! You can now log in.")
            window.destroy()