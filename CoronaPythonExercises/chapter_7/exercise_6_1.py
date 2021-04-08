prompt = "\nEnter a topping:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"You added {topping} to your pizza.")