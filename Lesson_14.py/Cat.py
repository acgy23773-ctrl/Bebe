class Cat:
    def __init__(self, poroda, color, name, sleeping, weight):

        self.poroda = poroda
        self.color = color
        self.name = name
        self.weight = 2
        self.sleeping = False

    def does_sleeping(self):
        if not self.sleeping:
            print("Isnt sleeping")
            return
        self.sleeping = True
        print("Is sleeping")


    def printInfo(self):
        print("="*10)
        print(f"Poroda: {self.poroda}")
        print(f"Color: {self.color}")
        print(f"Name: {self.name}")
        print(f"State: {self.does_sleeping}")
        print(f"Weight: {self.weight}")
        print("Мяу "*30)
        print("="*10)
