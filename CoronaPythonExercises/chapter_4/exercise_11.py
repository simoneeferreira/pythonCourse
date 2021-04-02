pizzas = ['marguerita', 'pepperoni', 'mushroom']
friend_pizzas = pizzas[:]
pizzas.append('diavola')
friend_pizzas.append('napoli')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print(f"My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
