import tkinter
from random import randint


class Calculator:
    def __init__(self):
        self.root = tkinter.Tk()
        # заголовок окна
        self.root.title("Калькулятор")
        # запрет на изменение размера окна
        self.root.resizable(False, False)
        # размер окна и место появления
        self.root.geometry("300x400+800+200")
        self.root["bg"] = "Gray"

        self.symbol_display = "0"
        self.symbol_little_display = ""
        self.little_display = tkinter.Label(self.root, font="Arial 8", width=47, bg="Gray",
                                            anchor="e", text=self.symbol_little_display)
        self.display = tkinter.Label(self.root, font="Arial 25", width=15,
                                     anchor="e", text=self.symbol_display,)
        self.little_display.place(relx=0.5, rely=0.02, anchor="n")
        self.display.place(relx=0.5, rely=0.06, anchor="n", height=65)
        self.frontend()

    # внешний вид
    def frontend(self):
        press_buttons = [
            "C", "<", "(", ")", "author",
            "7", "8", "9", "/", "random",
            "4", "5", "6", "*", "⎷",
            "1", "2", "3", "-", "x^2",
            "0", "00", ".", "+", "=",
        ]

        # вывод кнопок
        x = 6
        y = 100
        for press_button in press_buttons:
            # нажатие кнопки
            press = lambda symbol=press_button: self.backend(symbol)
            # рисую кнопки
            if press_button in ("random", "author"):
                font_size = 9
            else:
                font_size = 22
            tkinter.Button(text=press_button, font=f"Arial {font_size}", command=press,
                           bg="White").place(x=x, y=y, width=53, height=53)
            x += 59
            if x > 250:
                x = 6
                y += 59

    # логика
    def backend(self, press):
        # кнопка вывода информации о авторе программы
        if press == "author":
            self.symbol_little_display = "Rybak Alexander - rybak.a87@gmail.com"
        # кнопка для вывода случайного числа
        elif press == "random":
            self.symbol_little_display = f"Сгенерировано случайное число от 0 до {self.symbol_display}"
            self.symbol_display = str(randint(0, eval(self.symbol_display)))
        # кнопка сброс
        elif press == "C":
            self.symbol_display = ""
            self.symbol_little_display = ""
        # кнопка удаления последнего символа
        elif press == "<":
            if len(self.symbol_display) > 15:
                self.symbol_little_display = ""
            self.symbol_display = self.symbol_display[:-1]
        # кнопка равно
        elif press == "=":
            try:
                self.symbol_little_display = self.symbol_display
                self.symbol_display = str(eval(self.symbol_display))
            except ZeroDivisionError:
                self.symbol_display = ""
                self.symbol_little_display = "Было замечена попытка деления на ноль"
        # кнопка квадратного корня
        elif press == "⎷":
            self.symbol_display = str(eval(self.symbol_display)**0.5)
        # кномпа второй степени
        elif press == "x^2":
            self.symbol_display = str(eval(self.symbol_display)**2)
        else:
            if self.symbol_display == "0":
                self.symbol_display = ""
            # проверка на вмещения информации на дисплей
            if len(self.symbol_display) < 16:
                self.symbol_display += press
            else:
                self.symbol_little_display = "Не помещается на экран"
        self.on_screen()

    # вывод нажатий на экран
    def on_screen(self):
        if self.symbol_display == "":
            self.symbol_display = "0"
        self.display["text"] = self.symbol_display[:16]
        self.little_display["text"] = self.symbol_little_display

    # запуск приложения
    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.start()
