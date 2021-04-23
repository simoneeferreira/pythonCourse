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

class Admin(User):

    def __init__(self, first_name, last_name, age, hobbie, gender):
        super().__init__(first_name, last_name, age, hobbie, gender)
        self.privileges = []
    
    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

anna = Admin('anna', 'souza', '25', 'football', 'female')
anna.describe_user()
anna.privileges = ["can add post", "can delete post", "can ban user"]
anna.show_privileges()