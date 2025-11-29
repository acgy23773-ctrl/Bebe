from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Фотки")
root.geometry('800x720')
root.resizable(width=False, height=False)

# imgs = {1: Image.open('/images/23.png'),
#         2: Image.open('images/sfsfs.png'),
#         3: Image.open('images/231.ping'),
#         4: Image.open('images/i.png'),
#         5: Image.open('images/ii.png'),}

# img_b1 = imgs[1].resize((150, 150))
# img_b1 = ImageTk.PhotoImage(img_b1)

# img_b2 = imgs[2].resize((150, 150))
# img_b2 = ImageTk.PhotoImage(img_b2)

# img_b3 = imgs[3].resize((150, 150))
# img_b4 = ImageTk.PhotoImage(img_b3)

# img_b4 = imgs[4].resize((150, 150))
# img_b4 = ImageTk.PhotoImage(img_b4)

# img_b5 = imgs[5].resize((150, 150))
# img_b5 = ImageTk.PhotoImage(img_b5)

# variant = {1: img_b1,
#            2: img_b2,
#            3: img_b3,
#            4: img_b4}

# var = IntVar()
# var.set(0)

# b1 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b1)
# b1.place(relx=0.1, rely=0.75)

# b2 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b2)
# b2.place(relx=0.1, rely=0.75)

sc1 = Scale(from_=50, to=400, length=400)
sc1.place(relx=0.18, rely=0.1)

sc2 = Scale(from_=50, to=400, length=400, orient='horizontal')
sc2.place(relx=0.25, rely=0.03)

canvas = Canvas(width=50, height=50, bg="grey")
canvas.place(relx=0.25, rely=0.1)











root.mainloop()