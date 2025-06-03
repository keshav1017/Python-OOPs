# initiate a class
class employee:
    # special method/magic method/ dunder method - contructor
    def __init__(self):
        print("Started executing data/attributes.")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data have been initiated.")
    
    def travel(self, destination):
        print("This travel method was called manually.")
        print(f"Employee is now travelling to {destination}.")

# creating an object/instance of class
sam = employee()

# print(sam.id)
# sam.travel("India")
print(type(sam))