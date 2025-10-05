
import tkinter


class RegisterView(tkinter.Toplevel):
    def __init__(self, user_controller):
        super().__init__()
        self.controller = user_controller
        self.title("Register")
        self.geometry("400x300")
        self.resizable(width=False, height=False)

        self.username_label = tkinter.Label(self, text="Username:")
        self.username_entry = tkinter.Entry(self)

        self.firstname_label = tkinter.Label(self, text="First Name:")
        self.firstname_entry = tkinter.Entry(self)

        self.lastname_label = tkinter.Label(self, text="Last Name:")
        self.lastname_entry = tkinter.Entry(self)

        self.password_label = tkinter.Label(self, text="Password:")
        self.password_entry = tkinter.Entry(self, show="*")


        self.register_button = tkinter.Button(self, text="Register", command=self.register_button_clicked)

        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.firstname_label.grid(row=1, column=0, padx=10, pady=10)
        self.firstname_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.lastname_label.grid(row=2, column=0, padx=10, pady=10)
        self.lastname_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.password_label.grid(row=3, column=0, padx=10, pady=10)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.register_button.grid(row=4, columnspan=2, pady=20)



    def register_button_clicked(self):
        username = self.username_entry.get()
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        password = self.password_entry.get()
        self.controller.handle_register(username, firstname, lastname, password, self)