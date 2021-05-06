filename = 'responses.txt'

print("Enter 'quit' when you finished.")

while True:
    name = input("What's your name?")
    
    if name == 'quit':
        break
    else:
        response = input("Why do you like preogramming?")
        if response == 'quit' or response == '':
            break
        else:
            with open(filename, 'a') as f:
                f.write(f"{name.title()}: {response}\n")
