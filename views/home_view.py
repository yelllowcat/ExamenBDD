import tkinter
from tkinter import ttk

class HomeView(tkinter.Toplevel):
    def __init__(self, user_controller, email ):
        super().__init__()
        self.title("Home")
        self.geometry("450x500")
        self.resizable(width=False, height=False)
        self.configure(bg="#f5f5f5")
        self.user_controller = user_controller
        self.username = user_controller.get_username(email)
        self.email = email
        self.id = user_controller.get_user_id(email)
        # Frame principal
        main_frame = tkinter.Frame(self, bg="#f5f5f5")
        main_frame.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

        # Título de bienvenida
        self.welcome_label = tkinter.Label(
            main_frame,
            text="¡Bienvenido!",
            font=("Arial", 18, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        self.welcome_label.pack(pady=(0, 10))

        # Nombre de usuario
        self.user_label = tkinter.Label(
            main_frame,
            text=f"Usuario: {self.username}",
            font=("Arial", 12),
            bg="#f5f5f5",
            fg="#34495e"
        )
        self.user_label.pack(pady=(0, 20))
        
        # Frame para cuentas
        accounts_frame = tkinter.LabelFrame(
            main_frame,
            text="Mis Cuentas",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            fg="#34495e",
            padx=15,
            pady=10
        )
        accounts_frame.pack(fill=tkinter.X, pady=(0, 20))
        
        self.accounts_listbox = ttk.Combobox(
            accounts_frame,
            state="readonly",
            font=("Arial", 10)
        )
        self.accounts_listbox.pack(fill=tkinter.X, ipady=5)
        self.user_controller.populate_user_accounts(self.email, self.accounts_listbox)
        print("Current User email in HomeView:", self.email)  # Debugging line
        # Frame para botones
        buttons_frame = tkinter.Frame(main_frame, bg="#f5f5f5")
        buttons_frame.pack(fill=tkinter.X)
        
        # Botón crear cuenta
        self.create_account_button = tkinter.Button(
            buttons_frame,
            text="Crear Cuenta",
            command=self.create_account,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tkinter.FLAT,
            cursor="hand2",
            height=2
        )
        self.create_account_button.pack(fill=tkinter.X, pady=(0, 10))

        # Botón transferir
        self.transfer_funds_button = tkinter.Button(
            buttons_frame,
            text="Transferir",
            command=self.transfer_funds(self.id),
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tkinter.FLAT,
            cursor="hand2",
            height=2
        )
        self.transfer_funds_button.pack(fill=tkinter.X, pady=(0, 10))
        
        # Botón consultar historial
        self.consult_balance_button = tkinter.Button(
            buttons_frame,
            text="Consultar Historial",
            command=self.consult_balance,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tkinter.FLAT,
            cursor="hand2",
            height=2
        )
        self.consult_balance_button.pack(fill=tkinter.X, pady=(0, 10))
        
        # Botón cerrar sesión
        self.logout_button = tkinter.Button(
            buttons_frame,
            text="Cerrar Sesión",
            command=self.logout,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            relief=tkinter.FLAT,
            cursor="hand2"
        )
        self.logout_button.pack(fill=tkinter.X)

        # Traer ventana al frente
        self.lift()
        self.focus_force()

    def logout(self):
        self.destroy()
        
    def create_account(self):
        self.user_controller.show_create_account_window()
    
    def transfer_funds(self,id):
        self.user_controller.show_transfer_funds_window(id)

    def consult_balance(self):
        self.user_controller.show_consult_balance_window()