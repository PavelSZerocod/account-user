class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"User {user.get_name()} добавлен.")
        else:
            print("Invalid user.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"User {user.get_name()} удален.")
                return
        print(f"No user found with ID {user_id}.")

    def list_users(self):
        for user in self._users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, "
                  f"Access Level: {user.get_access_level()}")


admin = Admin(1, "Павел")
user1 = User(2, "Макар")
user2 = User(3, "Елена")

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(2)
admin.list_users()