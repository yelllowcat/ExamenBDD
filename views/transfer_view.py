import tkinter
from tkinter import ttk, messagebox

class TransferView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Transferir Fondos")
        self.geometry("450x450")
        self.resizable(width=False, height=False)
        self.configure(bg="#f5f5f5")
        self.controller = user_controller

        # Frame principal
        main_frame = tkinter.Frame(self, bg="#f5f5f5")
        main_frame.pack(pady=30, padx=30, fill=tkinter.BOTH, expand=True)

        # Título
        title_label = tkinter.Label(
            main_frame,
            text="Transferir Fondos",
            font=("Arial", 16, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 25))

        # Monto
        amount_label = tkinter.Label(
            main_frame,
            text="Monto:",
            font=("Arial", 11),
            bg="#f5f5f5",
            anchor="w"
        )
        amount_label.pack(fill=tkinter.X, pady=(0, 5))

        self.amount_entry = tkinter.Entry(
            main_frame,
            font=("Arial", 11),
            relief=tkinter.SOLID,
            borderwidth=1
        )
        self.amount_entry.pack(fill=tkinter.X, pady=(0, 15), ipady=5)

        # Cuenta destino
        transfer_to_label = tkinter.Label(
            main_frame,
            text="Transferir a (ID de Cuenta):",
            font=("Arial", 11),
            bg="#f5f5f5",
            anchor="w"
        )
        transfer_to_label.pack(fill=tkinter.X, pady=(0, 5))

        account_options = self.controller.get_all_account_ids()
        self.transfer_to_combobox = ttk.Combobox(
            main_frame,
            values=account_options,
            state="readonly",
            font=("Arial", 11)
        )
        self.transfer_to_combobox.pack(fill=tkinter.X, pady=(0, 15), ipady=3)

        # Nota
        note_label = tkinter.Label(
            main_frame,
            text="Nota (opcional):",
            font=("Arial", 11),
            bg="#f5f5f5",
            anchor="w"
        )
        note_label.pack(fill=tkinter.X, pady=(0, 5))

        self.note_entry = tkinter.Entry(
            main_frame,
            font=("Arial", 11),
            relief=tkinter.SOLID,
            borderwidth=1
        )
        self.note_entry.pack(fill=tkinter.X, pady=(0, 25), ipady=5)

        # Botón transferir
        self.transfer_button = tkinter.Button(
            main_frame,
            text="Transferir",
            command=self.transfer,
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tkinter.FLAT,
            cursor="hand2",
            height=2
        )
        self.transfer_button.pack(fill=tkinter.X, pady=(0, 10))

        # Botón cerrar sesión
        self.logout_button = tkinter.Button(
            main_frame,
            text="Cerrar",
            command=self.logout,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            relief=tkinter.FLAT,
            cursor="hand2"
        )
        self.logout_button.pack(fill=tkinter.X)

    def transfer(self):
        amount = self.amount_entry.get()
        to_account_id = self.transfer_to_combobox.get()
        
        if not amount or not to_account_id:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        if self.controller.handle_transfer(amount, from_account_id=1, to_account_id=to_account_id, note=self.note_entry.get()):
            messagebox.showinfo("Éxito", f"Transferencia de ${amount} a la cuenta {to_account_id} realizada con éxito.")
            self.destroy()
        else:
            messagebox.showerror("Error", "Error al realizar la transferencia.")

    def logout(self):
        self.destroy()