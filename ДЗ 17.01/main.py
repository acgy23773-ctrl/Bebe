from funcs import *


blizhnik = Character("ближник", 70)
luchnil = Archer("дальник", 50, 1)

print(f"{blizhnik.name} hp: {blizhnik.hp}")
blizhnik.take_damage(30)
print(f"{blizhnik.name} hp до: {blizhnik.hp}")
blizhnik.heal(20)
print(f"{blizhnik.name} hp теперь: {blizhnik.hp}")
print("="*10)

print(f"{luchnil.name} hp: {luchnil.hp}, стрел: {luchnil.arrows}")
luchnil.shoot()
luchnil.shoot()
