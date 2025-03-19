'''
A class constructor is a special method or function that is used to create and initialize a new object from a class. 
Define the class constructor __init__() for a new class Villager that represents characters in the game Animal Crossing. 
The constructor accepts three required arguments: strings name, species, and catchphrase. The constructor defines four properties for a Villager:

name, a string initialized to the argument name
species, a string initialized to the argument species
catchphrase, a string initialized to the argument catchphrase
furniture, a list initialized to an empty list
'''
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        
    def add_item(self, item_name):
        if item_name == "acoustic guitar" or item_name ==  "ironwood kitchenette" or item_name== "ratten armchair" or item_name ==  "kotatsu" or item_name ==  "cacao tree":
            self.furniture.append(item_name)
    
    def of_personality_type(self, townies, personality_type):
        return [person.name for person in townies if person.personality == personality_type]
        
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)
