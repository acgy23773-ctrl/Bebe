class Shkolnik:
    def __init__(self, imya, vozrast, klass, uspevaemost, nazvanie_shkoly):
        self.imya = imya
        self.vozrast = vozrast
        self.klass = klass
        self.uspevaemost = uspevaemost
        self.nazvanie_shkoly = nazvanie_shkoly
        self.ocenki = []
        self.uroki = []

    def idti_v_shkolu(self):
        print(f"{self.imya} пошел в школу {self.nazvanie_shkoly}.")

    def idti_domoy(self):
        print(f"{self.imya} пошел домой.")

    def poluchit_ocenku(self, ocenka):
        self.ocenki.append(ocenka)
        print(f"Получена оценка: {ocenka}. Текущие оценки: {self.ocenki}")

    def dobavit_urok(self, urok):
        self.uroki.append(urok)
        print(f"Урок '{urok}' добавлен в список. Список уроков: {self.uroki}")

    def smenit_shkolu(self, novaya_shkola):
        self.nazvanie_shkoly = novaya_shkola
        print(f"Школа изменена на: {self.nazvanie_shkoly}")

    def printInfo(self):
        print("="*10)
        print(f"Имя: {self.imya}")
        print(f"Возраст: {self.vozrast}")
        print(f"Оценки: {self.ocenki}")
        print(f"Успеваемость: {self.uspevaemost}")
        print(f"Название школы: {self.nazvanie_shkoly}")
        print("="*10)