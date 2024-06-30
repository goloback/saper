from tkinter import*
class win_table():
    def __init__(self, data, level, time):
        self.data = data
        self.level = level
        self.time = time
        self.create_window()

    def create_window(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=350, height=250, bg='gray')
        self.canvas.pack()
        self.window.resizable(0, 0)
        self.canvas.create_text(20, 20, text='write your name', anchor=NW, font=(None, 25), fill='#5F1540')
        self.entry = Entry(self.canvas, font=(None, 25), width=15)
        self.entry.place(x=20, y=60)
        self.btn = Button(self.canvas, font=(None, 25), text='save')
        self.btn.place(x=140, y=100)