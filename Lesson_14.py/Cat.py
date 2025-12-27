class Cat:
    def __init__(self, poroda, color, name):
        self.poroda = poroda
        self.color = color
        self.name = name
        self.sleeping = False

    def does_sleeping(self):
        if self.sleeping:
            print("Is sleeping")
            return
        self.sleeping = True
        print("Isnt sleeping")


    def printInfo(self):
        print("="*10)
        print(f"Poroda: {self.poroda}")
        print(f"Color: {self.color}")
        print(f"Name: {self.name}")
        print(f"State: {self.does_sleeping}")
        print(f"Weight: {self.weight}")
        print("Мяу "*30)
        print("="*10)
