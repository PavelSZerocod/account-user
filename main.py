class User():

    def __init__(self, id, name, access_level_user):
        self.id = id
        self._name = name
        self.__access_level_user = access_level_user


class Admin(User):

    def __init__(self, id, name, access_level_user, access_level_admin):
        super().__init__(id, name, access_level_user)
        self.admin = access_level_admin
        self.task_user = []

    def add_user(self, id, name, access_level_user):
        new_user = User(id, name, access_level_user)
        self.task_user.append(new_user)

    def remove_user(self, id):
        user_to_remove = None
        for user in self.task_user:
            if user.id == id:
                user_to_remove = user
                break
        if user_to_remove:
            self.task_user.remove(user_to_remove)
            print(f"Пользователь с id {id} успешно удален.")
        else:
            print(f"Пользователь с id {id} не найден в списке.")

