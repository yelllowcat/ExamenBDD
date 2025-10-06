import tkinter

from _curses import window
from views.loginView import LoginView
from views.register_view import RegisterView
from views.home_view import HomeView
from views.create_account_view import CreateAccountView
from views.transfer_view import TransferView as TransferFundsView
from views.consult_history_view import ConsultHistoryView 
from tkinter import messagebox

class UserController():
    def __init__(self, user_model):
        self.user_model = user_model
        self.login_view = None
        self.register_view = None
        self.home_view = None  # <-- Add this line
        self.create_account_view = None
        self.transfer_funds_view = None
        self.consult_balance_view = None

    def run(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def show_register_window(self):
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = RegisterView(self)
        self.register_view.lift()

    def show_home_window(self):
        if self.home_view is None or not self.home_view.winfo_exists():
            self.home_view = HomeView(self)
        self.home_view.lift()
        
    def handle_register(self, username, firstname, lastname, password, window):
        if not all([username, firstname, lastname, password]):
            messagebox.showerror("Error", "Todos los campos son obligatorios!")
            return
        
        if self.user_model.create_user(username, firstname, lastname, password):
            messagebox.showinfo("Success", "User registered successfully! You can now log in.")
            window.destroy()

    def handle_login(self, username, password, window):
        if not all([username, password]):
            messagebox.showerror("Error", "Both fields are required!")
            return
        
        if self.user_model.authenticate_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            window.withdraw()
            self.show_home_window()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def handle_create_account(self, initial_balance, user_id):
        if self.user_model.open_account(initial_balance, user_id):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Error creating account.")
    
    def show_create_account_window(self):
        self.create_account_view = CreateAccountView(self)
        self.create_account_view.mainloop()

    def show_transfer_funds_window(self):
        self.transfer_funds_view = TransferFundsView(self)
        self.transfer_funds_view.mainloop()

    def show_consult_balance_window(self):
        self.consult_balance_view = ConsultHistoryView(self)
        self.consult_balance_view.mainloop()
        
    def get_all_account_ids(self):
        return self.user_model.get_all_account_ids()

    def handle_transfer(self, amount, from_account_id, to_account_id, note):
        if not all([amount, from_account_id, to_account_id]):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        if self.user_model.make_transfer(from_account_id, to_account_id, amount, note):
            messagebox.showinfo("Éxito", f"Transferencia de {amount} a la cuenta {to_account_id} realizada con éxito.")
        else:
            messagebox.showerror("Error", "Error al realizar la transferencia.")

    def get_transaction_history(self):
        return self.user_model.get_transaction_history()
    
   