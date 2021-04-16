send_messages = ['Congratulations on another year well lived.', 'Best wishes on your birthday.', 'Happy Birthday']
sent_messages = []

while send_messages:
    current_message = send_messages.pop()
    print(f"Sending message: {current_message}")
    sent_messages.append(current_message)

print("\nThe following messages have been sent:")
for sent_message in sent_messages:
    print(sent_message)

print(send_messages)
print(sent_messages)