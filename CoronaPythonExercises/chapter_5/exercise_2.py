#test 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#Equality
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#Inequality
if car != 'audi':
    print("It's not my car. I have a subaru.")
#lower case
print(car.lower() == 'subaru')

#test 2
age = 20
print("\nIs age == 20? I predict True.")
print(age == 20)
print("\nIs age == 27? I predict False.")
print(age == 27)

#numerical test
print(age >= 50)
print(age <= 40)
print(age == 20)
print(age != 30 )

#and/or keyword
print(age > 10 and age < 15)
print(age >= 10 or age <= 15)

#test 3
name = 'simone'
print("\nIs name == 'simone'? I predict True.")
print(name == 'simone')
print("\nIs name == 'joana'? I predict False.")
print(name == 'joana')

#test 4
animal = 'dog'
print("\nIs animal == 'dog'? I predict True.")
print(animal == 'dog')
print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')

#test 5
name = 'joao'
print("\nIs name == 'joao'? I predict True.")
print(name == 'joao')
print("\nIs name == 'marcos'? I predict False.")
print(name == 'marcos')

#test 6
animals = ['dog', 'cat', 'monkey', 'fish']
print('fish' in animals)
print('dog' not in animals)