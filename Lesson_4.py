# # age = 
# # while age < 18:
# #     print ("Ура я ребенок!")
# #     age += 1
# # print("Пора в армию")
# #  1 Задание
# counter = 1
# text = "Какой нибудь текст"
# while counter <= 10:
#     print(counter,text)
#     counter += 1
# 2 Задание
# allMoney = 110
# cost = 20
# while(allMoney >= cost):
#     allMoney -= cost
#     print("Вы купили что-то")
# print(f"У вас осталось {allMoney} рублей")
# 3 Задача
# randomNumber = 4
# inputNumber = int(input("Угадай число: "))

# while(randomNumber != inputNumber):
#     if(randomNumber > inputNumber):
#         print("Больше") 
#     else :
#         print("Меньше")
#     inputNumber = int(input("Заново: "))
    
    
# print("Ты угадал :)")
# Цикл 
# number = int(input("Введите число: "))
# summa = 0
# for i in range(1,number + 1):
#     summa += i

# print(f" от 0 до {number} = {summa}")
number = int(input("Введите число: "))
summa = 1
for i in range(1,number + 1):
    summa *= i

print(f" от 0 до {number} = {summa}")