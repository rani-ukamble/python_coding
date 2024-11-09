class RobotDog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("Bow bow")

# Main program

myDog = RobotDog("Rambo")
print(myDog.name)
myDog.bark()

        