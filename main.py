from controller.userController import UserController
from models.users_model import UserModel
if __name__ == '__main__':
    userModel = UserModel()
    userController = UserController(userModel)
    userController.run()