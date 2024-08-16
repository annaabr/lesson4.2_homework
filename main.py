class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # Приватный атрибут
        self.__name = name         # Приватный атрибут
        self.__access_level = 'user'  # Уровень доступа по умолчанию

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_access_level(self, value):
        self.__access_level = value

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def print_info(self):
        print()
        print(f"Имя: {self.__name}")
        print(f"ID: {self.__user_id}")
        print(f"Уровень доступа: {self.__access_level}")


class Admin(User):
    def __init__(self, user_id, name, admin_level = "super"):
        super().__init__(user_id, name)
        super().set_access_level('admin')  # Уровень доступа для администраторов
        self.admin_level = admin_level  # Дополнительный уровень доступа

    def add_user(self, user_list, user):
        if not isinstance(user, Admin):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print(f"Ошибка: пользователь {user.get_name()} ({user.get_access_level()}) не добавлен в систему, \nтак как можно добавлять только экземпляры класса User.")

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"Пользователь {user.get_name()} удален из системы.")
        else:
            print(f"Ошибка: пользователь {user.get_name()} не найден в системе.")

    def print_info(self):
        super().print_info()
        print(f"Я, {self.get_name()}, АДМИНИСТРАТОР! УРААА!!!")
        print()

user_list = []

print("\nСоздание пользователей и администратора:")

user1 = User("A103", "Иван Иванов")
user2 = User("R2222", "Петр Петров")
admin = Admin("G123H55", "Алексей Алексеев")

user1.print_info()
user2.print_info()
admin.print_info()

print("Имена пользователей меняем на фамилию и инициалы:")
user1.set_name("Иванов И.И.")
user2.set_name("Петров П.П.")
admin.set_name("Алексеев А.А.")

user1.print_info()
user2.print_info()
admin.print_info()

print("Администратор добавляет пользователей, пытается добавить себя:")
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, admin)

print("\nСписок пользователей:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

print(f"\nАдминистратор удаляет пользователя {user1.get_name()}:")
admin.remove_user(user_list, user1)

print(f"\nАдминистратор пытается повторно удалить пользователя {user1.get_name()}:")
admin.remove_user(user_list, user1)

print("\nСписок пользователей после удаления:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")