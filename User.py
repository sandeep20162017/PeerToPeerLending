from pymongo import MongoClient

class User:
    def __init__(self, user_id, username, password, email, balance):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.balance = balance

    def register(self):
        """Register a new user by inserting the user details into the 'users' collection."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        users = db.users

        user_data = {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'balance': self.balance
        }
        users.insert_one(user_data)
        client.close()
        print("User registered successfully.")

    def login(self):
        """Authenticate the user based on the provided credentials."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        users = db.users

        query = {'username': self.username, 'password': self.password}
        result = users.find_one(query)
        if result:
            print("User logged in successfully.")
        else:
            print("Invalid username or password.")
        client.close()
