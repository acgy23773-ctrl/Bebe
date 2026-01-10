class Cat:
    def __init__(self, name, age, poroda):
        self.__name = name
        self.__age = age
        self.__poroda = poroda
        
    def printInfo(self):
        print("=-= Информация о кошкe =-=")
        print(f"Name: {self.__name}")
        print(f"Let: {self.__age}")
        print(f"Poroda: {self.__poroda}")

    def speak(self):
        print("Кошка mauka")

class Dog:

    def __init__(self, name, age, poroda):
        self.__name = name
        self.__age = age
        self.__poroda = poroda
        
    def printInfo(self):
        print("=-= Информация о собке =-=")
        print(f"Name: {self.__name}")
        print(f"Let: {self.__age}")
        print(f"Poroda: {self.__poroda}")

    def speak(self):
        print("собака мяукает")

class HomeCat(Cat):
    def __init__(self, name, age, poroda, color, owner):
        super().__init__(name, age, poroda)
        self._color = color
        self._owner = owner
        self._is_sleeping = False
    
    def printInfo(self):
        super().printInfo()
        print(f"cvet: {self._color}")
        print(f"vladelec: {self._owner}")
        print(f"="*10)

    def play(self):
        if self._is_sleeping:
            print("koshka spit and ne mozhet igrat")
            return
        print("koshka nachinaet igrat")