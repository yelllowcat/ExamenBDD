import mysql.connector
from mysql.connector import Error, IntegrityError
from tkinter import messagebox

from config.db import DB_CONFIG

# Make sure to install mysql-connector-python
class DBConnector:
    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            if conn.is_connected():
                return conn
        except Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
            return None