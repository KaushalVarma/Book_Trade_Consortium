import hashlib

class UserManager:
    def __init__(self):
        self.users = {}  # Example user storage

    def register_user(self, name, email, password):
        user_id = len(self.users) + 1
        hashed_password = self._hash_password(password)
        self.users[user_id] = {'name': name, 'email': email, 'password': hashed_password}
        return user_id

    def get_user(self, user_id):
        return self.users.get(user_id, None)
    
    def login_user(self, email, password):
        hashed_password = self._hash_password(password)
        for user_id, user in self.users.items():
            if user['email'] == email and user['password'] == hashed_password:
                return user_id
        return None

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def reset_password(self, user_id, new_password):
        if user_id in self.users:
            hashed_password = self._hash_password(new_password)
            self.users[user_id]['password'] = hashed_password
            return True
        return False