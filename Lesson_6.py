# # 1 Задача Работа со списками
# Fruits = ["apple", "banana", "cherry"]
# Fruits.append("orange")
# Fruits.insert(1, "lemon") 
# Fruits.remove("banana")
# Fruits.count(len)
# print(Fruits)

# 2.1 Задача
# import math 
# part_1_1 = math.cos(aa.pi/3) + math.log2(16)
# part_1_2 = sum([math.factorial(n) + 1 for n in range (0,4)])
# part_1 = part_1_1 * part_1_2
# # print(part1)

# # 2.2 Задача
# part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)
# part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)
# result = part_1 + part_2 - part_3
# print(result)

# import random

# life = 5
# rand_num = random.randint(1,50)
# isWin = False

# print("Угадай число от 1 до 50")
# while life != 0:
#     num = int(input("Введи число: "))

#     if num == rand_num:
#         print("Угадал")
#         isWin = False
#         break

#     elif num < rand_num:
#         print("Число больше")
#         life -= 1

#     elif num > rand_num:
#         print("Число меньше")
#         life -= 1
# if(not isWin):
#     print("Вы проиграли")
