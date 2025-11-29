# def Convert(metrics1, metricks2, value, result):
    
#     if len(metrics1) == 0 or len(metricks2) ==0:
#         result.config(text="Одно из значений не выбрано")
    
#     elif not value.isdigit():
#         result.config(text="В строке нечислимые символы")
#     elif metrics1 == "мм":
#         if metricks2 == "мм":
#             result.config(text="Результат: " + value)
#         elif metricks2 == "см":
#             result.config(text="Результат: " + str(int(value) / 10))
#         elif metricks2 == "дц":
#             result.config(text="Результат: " + str(int(value) / 100))
#         elif metricks2 == "м":
#             result.config(text="Результат: " + str(int(value) / 1000))
#         elif metricks2 == "км":
#             result.config(text="Результат: " + str(int(value) / 1000000))