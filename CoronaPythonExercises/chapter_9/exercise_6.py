class Restaurant:

    def __init__(self, name, cuisine_type):
      self.name = name
      self.cuisine_type = cuisine_type
      self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")
    
    def set_number_served(self, number_served):
         self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

#big_one = IceCreamStand('The Big One')
#big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

#big_one.describe_restaurant()
#big_one.show_flavors()