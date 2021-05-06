filename = 'guest_book.txt'
import time

print("Enter 'quit' when you finished.")

while True:

    name = input("What's your name?")
    if name == 'quit':
        break

    else:
        with open(filename, 'a') as f:
            f.write(f"{name}, {time.ctime()}\n")
        print(f"{name.title()}, welcome!\n")