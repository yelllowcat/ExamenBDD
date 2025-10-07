import os
from pathlib import Path
from controller.userController import UserController
from models.users_model import UserModel
if not Path('.env').exists():
    print("Por favor, crea un archivo .env con la configuración de la base de datos")
    exit()
if __name__ == '__main__':
    userModel = UserModel()
    userController = UserController(userModel)
    userController.run()