class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user1 = User(1, "bilol")
user1.id = 10
user1.username = "Bilol"
print(user1.id)
