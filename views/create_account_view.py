import tkinter

class CreateAccountView(tkinter.Tk):
    def __init__(self, user_controller, id):
        super().__init__()
        self.title("Crear Cuenta")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.controller = user_controller
        self.id = id

        self.welcome_label = tkinter.Label(self, text="Bienvenido a la página de creación de cuentas!")
        self.welcome_label.pack(pady=20)

        self.balance_label = tkinter.Label(self, text="Saldo Inicial:")
        self.balance_label.pack(pady=5)
        self.balance_entry = tkinter.Entry(self)
        self.balance_entry.pack(pady=5)

        self.create_button = tkinter.Button(self, text="Crear Cuenta", command=self.create_account)
        self.create_button.pack(pady=10)

        self.close_button = tkinter.Button(self, text="Cerrar", command=self.close)
        self.close_button.pack(pady=10)

    def close(self):
        self.destroy()
        # Bring back HomeView and optionally refresh accounts
        try:
            if self.controller.home_view is not None and self.controller.home_view.winfo_exists():
                try:
                    # Safe refresh (in case HomeView has the helper)
                    self.controller.home_view.refresh_accounts()
                except Exception:
                    pass
                self.controller.home_view.lift()
                self.controller.home_view.focus_force()
        except Exception:
            pass
    
    def create_account(self):
        initial_balance = self.balance_entry.get()
        if not initial_balance:
            tkinter.messagebox.showerror("Error", "Todos los campos son obligatorios!")
            return
        try:
            initial_balance = float(initial_balance)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Saldo inicial debe ser un número y ID de usuario debe ser un entero!")
            return
        self.controller.handle_create_account(initial_balance, self.id)
        
        