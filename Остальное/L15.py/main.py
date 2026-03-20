from animals import *

def info(object):
    object.printInfo()

def animalSpeak(object):
    object.speak()

def play(object):
    object.play()
cat = Cat("лайt", 4, "seriy")
dog = Dog("brawl stars", 9, "pumba")
newcat = HomeCat("zhopa", 5, "volosataya", "krasnaya", "maksim")

info(cat)
info(dog)
info(newcat)
animalSpeak(cat)
animalSpeak(dog)
animalSpeak(newcat)
play(newcat)
