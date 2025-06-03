# initiate a class
class employee:
    # special method/magic method/ dunder method - contructor
    def __init__(self):
        print(id(self))
        # print("Started executing data/attributes.")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("Attributes/data have been initiated.")
    
    def travel(destination):
        print("This travel method was called manually.")
        print(f"Employee is now travelling to {destination}.")

# creating an object/instance of class
sam = employee()
sam.name = "Sam Kumar"
# print(id(sam))
# sam2 = employee()
# print(id(sam2))
print(sam.name)

# print(sam.id)
# sam.travel("India")