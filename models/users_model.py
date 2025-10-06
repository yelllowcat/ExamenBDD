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
            cursor.callproc("registrar_usuario", args)
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
        
    
    def authenticate_user(self, username, password):
        conn = DBConnector.get_connection()
        if conn is None:
            return False
        try:
            cursor = conn.cursor()
            args = (username, password);
            cursor.callproc("iniciar_sesion", args)
            for result in cursor.stored_results():
                user = result.fetchone()
                if user:
                    return True
                else:
                    return False
        except Exception as e:
            messagebox.showerror("Database Error", f"Error authenticating user: {e}")     
            return False
        finally:
            if conn.is_connected(): 
                conn.close()

    def open_account(self, initial_balance, user_id):
        conn = DBConnector.get_connection()
        if conn is None:
            return False
        try:
            cursor = conn.cursor()
            args = (initial_balance, user_id);
            cursor.callproc("abrir_cuenta", args)
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror("Database Error", f"Error creating account: {e}")     
            return False
        finally:
            if conn.is_connected(): 
                conn.close()
    
    def get_user_details(self, username):
        conn = DBConnector.get_connection()
        if conn is None:
            return None
        try:
            cursor = conn.cursor()
            args = (username,);
            cursor.callproc("obtener_detalles_usuario", args)
            for result in cursor.stored_results():
                user = result.fetchone()
                if user:
                    return {
                        "username": user[0],
                        "firstname": user[1],
                        "lastname": user[2]
                    }
                else:
                    return None
        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching user details: {e}")     
            return None
        finally:
            if conn.is_connected(): 
                conn.close()
                
    def get_all_account_ids(self):
        conn = DBConnector.get_connection()
        if conn is None:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM cuentas")  # Adjust table/column names as needed
            accounts = cursor.fetchall()
            return [account[0] for account in accounts]
        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching account IDs: {e}")     
            return []
        finally:
            if conn.is_connected(): 
                conn.close()
                
    def make_transfer(self, from_account_id, to_account_id, amount, note):
        conn = DBConnector.get_connection()
        if conn is None:
            return False
        try:
            cursor = conn.cursor()
            args = (from_account_id, to_account_id, amount, note);
            cursor.callproc("transferir_dinero", args)
            conn.commit()
            return True
        except Exception as e:
            messagebox.showerror("Database Error", f"Error making transfer: {e}")     
            return False
        finally:
            if conn.is_connected(): 
                conn.close()
                
    def get_transaction_history(self):
        conn = DBConnector.get_connection()
        if conn is None:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    id, 
                    tipo_movimiento, 
                    cuenta_salida_id, 
                    cuenta_entrada_id, 
                    monto, 
                    fecha_operacion, 
                    nota 
                FROM movimientos 
                ORDER BY fecha_operacion DESC
            """)

            transactions = cursor.fetchall()
            return transactions  # Devuelve las tuplas directamente

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching transaction history: {e}")     
            return []
        finally:
            if conn.is_connected(): 
                conn.close()
                
  