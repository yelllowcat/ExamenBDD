import tkinter
from tkinter import ttk

class ConsultHistoryView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Consultar Historial")
        self.geometry("900x500")
        self.resizable(width=True, height=True)
        self.controller = user_controller

        # Título
        self.history_label = tkinter.Label(
            self, 
            text="Historial de Transacciones:",
            font=("Arial", 14, "bold")
        )
        self.history_label.pack(pady=10)

        # Frame para el Treeview y scrollbar
        tree_frame = tkinter.Frame(self)
        tree_frame.pack(pady=10, padx=10, fill=tkinter.BOTH, expand=True)

        # Scrollbar vertical
        scrollbar_y = tkinter.Scrollbar(tree_frame, orient=tkinter.VERTICAL)
        scrollbar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Scrollbar horizontal
        scrollbar_x = tkinter.Scrollbar(tree_frame, orient=tkinter.HORIZONTAL)
        scrollbar_x.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        # Treeview con columnas
        columns = ("ID", "Tipo", "Cuenta Salida", "Cuenta Entrada", "Monto", "Fecha", "Nota")
        self.history_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        # Configurar scrollbars
        scrollbar_y.config(command=self.history_tree.yview)
        scrollbar_x.config(command=self.history_tree.xview)

        # Configurar encabezados y ancho de columnas
        self.history_tree.heading("ID", text="ID")
        self.history_tree.heading("Tipo", text="Tipo")
        self.history_tree.heading("Cuenta Salida", text="Cuenta Salida")
        self.history_tree.heading("Cuenta Entrada", text="Cuenta Entrada")
        self.history_tree.heading("Monto", text="Monto")
        self.history_tree.heading("Fecha", text="Fecha")
        self.history_tree.heading("Nota", text="Nota")

        self.history_tree.column("ID", width=50, anchor=tkinter.CENTER)
        self.history_tree.column("Tipo", width=150, anchor=tkinter.CENTER)
        self.history_tree.column("Cuenta Salida", width=100, anchor=tkinter.CENTER)
        self.history_tree.column("Cuenta Entrada", width=100, anchor=tkinter.CENTER)
        self.history_tree.column("Monto", width=100, anchor=tkinter.E)
        self.history_tree.column("Fecha", width=150, anchor=tkinter.CENTER)
        self.history_tree.column("Nota", width=200, anchor=tkinter.W)

        self.history_tree.pack(fill=tkinter.BOTH, expand=True)

        # Alternar colores de filas
        self.history_tree.tag_configure("oddrow", background="#f0f0f0")
        self.history_tree.tag_configure("evenrow", background="#ffffff")

        # Cargar datos
        self.load_history()

        # Botón para cerrar
        close_button = tkinter.Button(
            self,
            text="Cerrar",
            command=self.destroy,
            width=15,
            bg="#dc3545",
            fg="white",
            font=("Arial", 10)
        )
        close_button.pack(pady=10)

    def load_history(self):
        """Cargar el historial de transacciones"""
        history = self.controller.get_transaction_history()
        
        for index, record in enumerate(history):
            # record debe ser una tupla con los 7 valores:
            # (id, tipo_movimiento, cuenta_salida_id, cuenta_entrada_id, monto, fecha_operacion, nota)
            
            # Formatear el monto con 2 decimales
            formatted_record = list(record)
            if len(formatted_record) >= 5:
                formatted_record[4] = f"${formatted_record[4]:,.2f}"
            
            # Alternar colores
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            
            self.history_tree.insert("", tkinter.END, values=formatted_record, tags=(tag,))