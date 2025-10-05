from models.db.db_connector import DBConnector
from tkinter import messagebox
from mysql.connector import IntegrityError

class UserModel:
    def __init__(self):
        pass
    
    def create_user(self, username, firstname, lastname, password):
        conn = DBConnector.get_connection()
        if conn is None:
            return False
        try:
            cursor = conn.cursor()
            args = (username, password, firstname, lastname);
            cursor.callproc("SP_STORE_USER", args)
            conn.commit()
            return True
        except IntegrityError as e:
            messagebox.showerror("Database Error", f"User with this username '{username}' already exists.")
            return False
        except Exception as e:
            messagebox.showerror("Database Error", f"Error creating user: {e}")     
            return False
        finally:
            if conn.is_connected(): 
                conn.close()