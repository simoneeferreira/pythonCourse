class User():
    def __init__(self, first_name, last_name, age, hobbie, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobbie = hobbie
        self.gender = gender
        self.login_attempts = 10
    
    def describe_user(self):
        summary = f"\nProfile\nName: {self.first_name.title()} {self.last_name.title()}\nAge: {self.age}\nGender: {self.gender.title()}\nHobbie: {self.hobbie}"
        print(summary)
    
    def greet_user (self):
        msg = f"Welcome back, {self.first_name}!"
        print(msg)
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

anna = User('anna', 'souza', '25', 'football', 'female')
anna.describe_user()
anna.greet_user()
print(anna.login_attempts)
anna.increment_login_attempts()
anna.increment_login_attempts()
anna.increment_login_attempts()
anna.increment_login_attempts()
print(anna.login_attempts)
anna.reset_login_attempts()
print(anna.login_attempts)