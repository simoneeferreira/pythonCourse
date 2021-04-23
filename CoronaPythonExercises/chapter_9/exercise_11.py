from exercise_8 import Admin

anna = Admin('anna', 'matthes', 'a_matthes', 'a_matthes@example.com', 'los angeles')
anna.describe_user()

anna.privileges.show_privileges()

print("\nAdding privileges...")
anna_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
anna.privileges.privileges = anna_privileges
anna.privileges.show_privileges()