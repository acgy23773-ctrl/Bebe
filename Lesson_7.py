# lst1 = [23, 57, 13, 67, 75]
# new_lst1 = []

# for i in lst1: 
#     new_lst1.append(i ** 2)

# result1 = sum(new_lst1)
# print(result1)


# lst2 = [14, 49, 6, 64]
# new_lst2 = []

# for i in lst2: 
#     new_lst2.append(i ** 2)


# result2 = sum(new_lst2)
# print(result2)

# lst3 = [8, 90, 55, 83, 1,22]
# new_lst3 = []

# for i in lst3: 
#     new_lst3.append(i ** 2)

# result3 = sum(new_lst3)
# print(result3)

# def sum_squares_nums(lst):
#     new_lst = [6, 9, 13]
#     for i in lst:
#         new_lst.append(i ** 2)

#     result = sum(new_lst)
#     return result

# lst1 = [23, 57, 13, 67, 75]

# result1 = sum_squares_nums(lst1)
# print(result1)


# lst2 = [14, 49, 6, 64]

# result2 = sum_squares_nums(lst1)
# print(result2)

# lst3 = [8, 90, 55, 83, 1, 22]

# result3 = sum_squares_nums(lst1)
# print(result3)

# import random
# import string

# def password_generation(lenPas, iSnums, isUpAlpha):
#     symbols = string.ascii_lowercase
#     password = ''
#     if isUpAlpha:
#         symbols += string.ascii_uppercase
#     if iSnums:
#         symbols += '1234567890'
#     for _ in range(lenPas):
#         password += random.choice(symbols)
#     return password

# print("Генерация пароля")
# lenPas = int(input("длина : "))
# iSnums = input("нужны ли цифры y/n : ")
# isUpAlpha = input("нужны ли большие буквы y/n : ")

# if iSnums.lower() == "y":
#     iSnums = True
# else:
#     iSnums = False

# if isUpAlpha.lower() == "y":
#     isUpAlpha = True
# else:
#     isUpAlpha = False

# password = password_generation(lenPas, iSnums, isUpAlpha)
# print(password)


# def NumberIsEven(number):
#     if number % 2 == 0:
#         return True;
#     else:
#         return False;
# if(NumberIsEven(10)):
#     print("10 Четное")


# def CountVowelsSymbols(text):
#     vowelsSymbols = "аеёиоуыэяй"
#     count = 0
#     for i in text:
#             count += vowelsSymbols.count(i)
#     return count
# print(CountVowelsSymbols("парампам пам буыыыдыдш"))


# def Sum(number):
#     strNumbers = str(number)
#     Summa = 0
#     for i in strNumbers:
#         Summa += int(i)
#     return Summa

# print(Sum(412364593993939399))