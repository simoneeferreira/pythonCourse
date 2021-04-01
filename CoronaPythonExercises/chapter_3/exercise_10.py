food = ['bread', 'pasta', 'meat', 'pumpkin', 'cheesecake', 'pizza', 'avocado', 'sushi', 'strawberrie', 'sausage', 'milk', 'rice', 'beans']

print(food[4])

food[3] = 'Potato'
print(food)

food.append('cake')
print(food)

food.insert(5, 'soup')
print(food)

del food[3]
print(food)

popped_food = food.pop()
print(popped_food)
print(food)

favourite = food.pop(1)
print(f"My favourite food is {favourite}.")
print(food)

food.remove('pizza')
print(food)

print(sorted(food))
print(food)

food.sort()
print(food)

food.sort(reverse=True)
print(food)

food.reverse()
print(food)

print(len(food))
