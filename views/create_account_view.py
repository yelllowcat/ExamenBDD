import tkinter

class CreateAccountView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Crear Cuenta")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.controller = user_controller

        self.welcome_label = tkinter.Label(self, text="Bienvenido a la página de creación de cuentas!")
        self.welcome_label.pack(pady=20)

        self.balance_label = tkinter.Label(self, text="Saldo Inicial:")
        self.balance_label.pack(pady=5)
        self.balance_entry = tkinter.Entry(self)
        self.balance_entry.pack(pady=5)

        self.user_id_label = tkinter.Label(self, text="ID de Usuario:")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tkinter.Entry(self)
        self.user_id_entry.pack(pady=5)

        self.create_button = tkinter.Button(self, text="Crear Cuenta", command=self.create_account)
        self.create_button.pack(pady=10)

        self.logout_button = tkinter.Button(self, text="Cerrar Sesión", command=self.logout)
        self.logout_button.pack(pady=10)

    def logout(self):
        self.destroy()
        self.controller.show_login_window()
    
    def create_account(self):
        initial_balance = self.balance_entry.get()
        user_id = self.user_id_entry.get()
        if not initial_balance or not user_id:
            tkinter.messagebox.showerror("Error", "Todos los campos son obligatorios!")
            return
        try:
            initial_balance = float(initial_balance)
            user_id = int(user_id)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Saldo inicial debe ser un número y ID de usuario debe ser un entero!")
            return
        self.controller.handle_create_account(initial_balance, user_id)
        
        