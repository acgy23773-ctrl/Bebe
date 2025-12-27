class Car:
    def __init__(self, name, color, power):
        self.name = name
        self.color = color
        self.power = power
        self.mileage = 0
        self.is_running = False

    def start_engine(self):
        if self.is_running:
            print("Engine is already running")
            return
        self.is_running = True
        print("Engine is running")

    def stop_engine(self):
        if not self.is_running:
            print("Engine is already off")
            return
        self.is_running = False
        print("Engine is off")

    def printInfo(self):
        print("="*10)
        print(f"Car name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Power: {self.power}")
        print("="*10)