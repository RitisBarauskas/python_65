class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.first_name = ''
        self.last_name = ''

    def __str__(self):
        return f'User: {self.username}'
