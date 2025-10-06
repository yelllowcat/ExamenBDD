import tkinter

class HomeView(tkinter.Toplevel):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Home")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.user_controller = user_controller

        self.welcome_label = tkinter.Label(self, text="Bienvenido!")
        self.welcome_label.pack(pady=20)

        self.create_account_button = tkinter.Button(self, text="Crear Cuenta", command=self.create_account)
        self.create_account_button.pack(pady=10)

        self.transfer_funds_button = tkinter.Button(self, text="Transferir", command=self.transfer_funds)
        self.transfer_funds_button.pack(pady=10)
        
        self.consult_balance_button = tkinter.Button(self, text="Consultar Historial", command=self.consult_balance)
        self.consult_balance_button.pack(pady=10)
        
        self.logout_button = tkinter.Button(self, text="Cerrar Sesión", command=self.logout)
        self.logout_button.pack(pady=10)
        

        # Bring window to front
        self.lift()
        self.focus_force()

    def logout(self):
        self.destroy()
        
    def create_account(self):
        self.user_controller.show_create_account_window()
    
    def transfer_funds(self):
        self.user_controller.show_transfer_funds_window()

    def consult_balance(self):
        self.user_controller.show_consult_balance_window()