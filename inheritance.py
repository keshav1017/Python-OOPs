# # simple inheritance

# ## Base Class
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound")

# ## Derived class
# class Dog(Animal):

#     def __init__(self):
#         self.behaviour = "friendly"

#     def speak1(self):
#         print(f"{self.name} barks. He is {self.behaviour}")

# # # create an instance of animal
# # animal = Animal("Genric Animal")
# # animal.speak()

# # Create an instance of dog
# dog = Dog()
# dog.speak()

# Super 

## Base Class
class Animal:
    def __init__(self):
        self.name = "Buddy"
    
    def speak(self):
        print(f"{self.name} makes a sound")

## derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}")

## create an instance of dog

dog = Dog("Golden Retriver")
dog.speak()

