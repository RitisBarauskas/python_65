class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.first_name = ''
        self.last_name = ''
        self.age = age


    def __str__(self):
        return f'User: {self.username}'
