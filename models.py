class User:
    def __init__(self, username, password,age):
        self.username = username
        self.password = password
        self.age = age


    def __str__(self):
        return f'User: {self.username}'
