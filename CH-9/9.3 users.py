class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")


fay = User('faysal', 'ahammed', 'fay90', 'fay90@example.com')
fay.describe_user()
fay.greet_user()

khair = User('khair', 'ahmed', 'khair90', 'khair90@example.com')
khair.describe_user()
khair.greet_user()
