class Restaurant():
    def __init__(self, name, cuisine_type):
      self.name = name
      self.cuisine_type = cuisine_type

    def describe_restaurant(self):
      msg = f"{self.name.title()} serves wonderful {self.cuisine_type}."
      print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name.title()} is open. Come on in!"
        print(f"\n{msg}")

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()