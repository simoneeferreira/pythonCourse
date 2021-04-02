#Exercise_12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

#Exercise_13
foods = ('rice', 'bean', 'beef', 'salad', 'mash potato')
print("Old menu:")
for food in foods:
    print(food)

# foods[2] = 'sushi'
foods = ('rice', 'mushroom', 'chicken', 'salad', 'mash potato')
print("\nNew menu:")
for food in foods:
    print(food)
#Exercise_2

animals = ['dog', 'fish', 'cat']
for animal in animals:
    print(animal)

for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")