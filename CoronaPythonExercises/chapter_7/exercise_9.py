sandwich_orders = ['pastrami', 'pepperoni', 'salami','pastrami',  'ham and cheese', 'pastrami', 'cheese']
finished_sandwiches = []

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiche = sandwich_orders.pop()

    print(f"\nI made your {current_sandwiche} sandwich.")
    finished_sandwiches.append(current_sandwiche)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())