
# First we will create a new PARENT Class, let' say a Toy class, this class will include the basic features of a toy like color and name.\

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Now we will make a method inside the PARENT Toy class namely - whatToy, this method will give us information about the toy.
    def whatToy(self):
        print(f"Meet {self.name}, the vibrant {self.color} color of {self.name} is loved by children all around the world!")

# Now, we came across a different type of a toy, it has legs! It's an animal and it makes some sound. Let's quickly code it.

class WildAnimal(Toy): #This WildAnimal will inherit from the Parent Toy class, because even the WildAnimal is a toy in this scenario, making it a child class.
    def __init__(self, name, color, legs, voice):
        super().__init__(name, color) #This will inherit the name and color variables from the parent toy class.
        # The WildAnimal has it's own unique number of legs and a fearsome voice! But the color and it's name are already defined in the parent class.
        self.legs = legs
        self.voice = voice

    def sound(self):
        print(f"Our friend {self.name} makes a {self.voice} sound!")
    
    def whatToy(self):
        super().whatToy()
        print(f"Hello kids! I have {self.legs} legs, and I will stay very loyal to you!")


wildAnimal = WildAnimal("Rufus", "Greyish - White", 4, "Ruff - Ruff")
wildAnimal.whatToy()
wildAnimal.sound()


