import os

def user_name():
    return os.getlogin()


print(user_name())