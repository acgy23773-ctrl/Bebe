from tkinter import *

class App:
    def __init__(self):
        self.__window = Tk()
        self.__width_window = 400
        self.__height_window = 500
        self.__screen_width = self.__window.winfo_screenwidth()
        self.__screen_height = self.__window.winfo_screenheight()
        self.__x = (self.__screen_width // 2) - (self.__width_window // 2)
        self.__y = (self.__screen_height // 2) - (self.__height_window // 2)
        self._name_app = "Сбер"