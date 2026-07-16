class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        print("user created")
    """Models the user."""
    pass

user_1 = User("001", "eniola")
print(user_1.id)
print(user_1.followers)


# print(user_1.name)
