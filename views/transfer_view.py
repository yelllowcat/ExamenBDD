import tkinter

class TransferView(tkinter.Tk):
    def __init__(self, user_controller):
        super().__init__()
        self.title("Transfer Funds")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.controller = user_controller

        self.amount_label = tkinter.Label(self, text="Amount:")
        self.amount_label.pack(pady=10)

        self.amount_entry = tkinter.Entry(self)
        self.amount_entry.pack(pady=10)

        self.transfer_button = tkinter.Button(self, text="Transfer", command=self.transfer)
        self.transfer_button.pack(pady=10)

    def transfer(self):
        amount = self.amount_entry.get()
        # Implement transfer logic here
        tkinter.messagebox.showinfo("Transfer", f"Transferring {amount}...")
        self.destroy()

    def logout(self):
        self.destroy()