current_users = ['maria', 'jOao', 'anna', 'pedro', 'marta']
new_users = ['jose', 'joao', 'viviane', 'pedro', 'jonh']

for new_user in new_users:
    if new_user in current_users:
        print(f"Username {new_user} already exist. Please enter a new username.")
    else:
        print(f"Username {new_user} available!")