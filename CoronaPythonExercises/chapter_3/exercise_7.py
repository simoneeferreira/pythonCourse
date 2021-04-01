guest = ['Ana', 'Paulo', 'Joao']

print(guest)

guest.insert(0, 'Cris')
guest.insert(3, 'Marta')
guest.append('Vivian')

print(guest)

print("I can invite only two people for dinner.")
pooped_guest = guest.pop()
print(f"Sorry {pooped_guest}, but I can\'t invite you to dinner")
pooped_guest = guest.pop()
print(f"Sorry {pooped_guest}, but I can\'t invite you to dinner")
pooped_guest = guest.pop()
print(f"Sorry {pooped_guest}, but I can\'t invite you to dinner")
pooped_guest = guest.pop()
print(f"Sorry {pooped_guest}, but I can\'t invite you to dinner")

message = f"Hi {guest[0]}, come have dinner with me."
print(message)
message = f"Hi {guest[1]}, come have dinner with me."
print(message)

del guest[0]
del guest[0]
print(guest)