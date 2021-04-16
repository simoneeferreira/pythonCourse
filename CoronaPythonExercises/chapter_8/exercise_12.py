def make_sandwich(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
make_sandwich('ham', 'cheese')