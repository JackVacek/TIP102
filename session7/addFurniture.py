class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
        
    def add_item(self, item_name):
        if item_name == "acoustic guitar" or item_name ==  "ironwood kitchenette" or item_name== "ratten armchair" or item_name ==  "kotatsu" or item_name ==  "cacao tree":
            self.furniture.append(item_name)

def of_personality_type(townies, personality_type):
    return [person.name for person in townies if person.personality == personality_type]

def message_received(start_villager, target_villager):
    while start_villager.neighbor:
        if start_villager.neighbor == target_villager:
            return True
        start_villager = start_villager.neighbor
    return False
    
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))