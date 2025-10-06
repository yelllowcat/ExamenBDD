import tkinter

class ConsultView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Consultar Saldo")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.controller = user_controller

        self.balance_label = tkinter.Label(self, text="Su saldo es:")
        self.balance_label.pack(pady=10)

        self.balance_amount = tkinter.Label(self, text="$0.00")
        self.balance_amount.pack(pady=10)

        self.logout_button = tkinter.Button(self, text="Cerrar Sesión", command=self.logout)
        self.logout_button.pack(pady=10)

    def logout(self):
        self.destroy()

  