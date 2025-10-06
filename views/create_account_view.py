import tkinter

class CreateAccountView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Crear Cuenta")
        self.geometry("400x200")
        self.resizable(width=False, height=False)
        self.controller = user_controller

        self.welcome_label = tkinter.Label(self, text="Bienvenido a la página de creación de cuentas!")
        self.welcome_label.pack(pady=20)

        self.logout_button = tkinter.Button(self, text="Cerrar Sesión", command=self.logout)
        self.logout_button.pack(pady=10)

    def logout(self):
        self.destroy()
        
        
        