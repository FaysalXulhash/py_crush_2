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


fay = User('faysal', 'ahammed', 'fay90', 'fay90@example.com')
fay.describe_user()
fay.greet_user()


print("\nMaking 3 login attempts...")
fay.increment_login_attempts()
fay.increment_login_attempts()
fay.increment_login_attempts()
print(f"  Login attempts: {fay.login_attempts}")

print("Resetting login attempts...")
fay.reset_login_attempts()
print(f"  Login attempts: {fay.login_attempts}")