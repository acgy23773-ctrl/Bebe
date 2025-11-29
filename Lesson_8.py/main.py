from tkinter import *
from tkinter import ttk
from funcs import Convert
metrics = ["мм", "см","дц", "м", "км"]

root = Tk()
root.title("Приложение")
root.geometry("500x400")

items1 = ttk.Combobox(values=metrics)
items1.place(relx=0.15, rely=0.1, width=150, height=30)

text1 = ttk.Label(text="из")
text1.place(relx=0.1,rely=0.11)

text2 = ttk.Label(text="В")
text2.place (relx=0.5,rely=0.11)

items2 = ttk.Combobox(values=metrics)
items2.place(relx=0.58, rely=0.1, width=150, height=30)

text3 = ttk.Label(text="Введите значение: ")
text3.place(relx=0.15, rely=0.3)

input_num = ttk.Entry()
input_num.place(relx=0.15, rely=0.4, width=150, height=30)

result = ttk.Label(text="Результат: ")
result.place(relx=0.55, rely=0.4)

convert = ttk.Button(text="Конвертировать",
    command=lambda: Convert(items1.get(), items2.get(), input_num.get(), result))

convert.place(relx=0.35, rely=0.6, width=150, height=50)


root.mainloop()