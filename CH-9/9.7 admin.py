class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email):

        super().__init__(first_name, last_name, username, email)
        self.privileges = []

    def show_privileges(self):

        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


fay = Admin('faysal', 'ahammed', 'fay90', 'fay90@example.com')
fay.describe_user()

fay.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

fay.show_privileges()
