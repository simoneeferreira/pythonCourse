prompt = "\nEnter your age:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
           print(f"\nYou are {age} years old, the ticket is free.")
        elif age >= 3 and age < 12:
             print(f"\nYou are {age} years old, the ticket is $10.")
        elif age >= 12:
             print(f"\nYou are {age} years old, the ticket is $15.")