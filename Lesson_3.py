# currentYear = 2025
# currentMonth = 10
# currentDay = 11

# print("Введите дату вашего рождения")

# birthYear = int(input("Год: "))
# birthMonth = int(input("Месяц: "))
# birthDay = int(input("День: "))

# age = currentYear - birthYear

# if currentMonth > birthMonth:
#     print(f"Вам {age} лет")
# elif currentMonth == birthMonth:
#     if currentDay > birthDay:
#         print(f"Вам {age} лет")
#     elif currentDay == birthDay:
#             print (f"С днем рождения!")
#     else : 
#          print (f"Вам {age} лет")
# else:
#     print(f"Вам {age - 1} лет")


# import random

# life = 5
# rand_num = random.randit(1,50)
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

# # ЧЕРЕПАХАААААААААААААААААААААААААААААААААААААААААААА
# import turtle

# screen = turtle.Screen()
# screen.setup(600, 600)
# screen.bgcolor("white")
# screen.title("Изучаем черепаху")
# t = turtle.Turtle()
# t.speed(5)
# t.width(3)
# t.penup()
# t.goto(0, -100)
# t.pendown()
# t.color("black", "yellow")
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.penup()
# t.goto(-40, 30)
# t.pendown()
# t.color("black", "white")
# t.begin_fill()
# t.circle(20)
# t.end_fill()

# t.penup()
# t.goto(-40, 40)
# t.pendown()
# t.color("black", "black")
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# t.penup()
# t.goto(40, 30)
# t.pendown()
# t.color("black", "white")
# t.begin_fill()
# t.circle(20)
# t.end_fill()

# t.penup()
# t.goto(40, 40)
# t.pendown()
# t.color("black", "black")
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# t.penup()
# t.goto(-60, -20)
# t.pendown()
# t.color("black")
# t.width(5)
# t.setheading(-60)
# t.circle(70, 120)
# t.hideturtle()



# screen.exitonclick()