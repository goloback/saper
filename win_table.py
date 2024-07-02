from tkinter import*
class win_table():
    def __init__(self, data, level, time):
        self.data = data
        self.level = level
        self.time = time
        self.create_window()

    def create_window(self):
        self.window = Tk()
        self.window.title("you won")
        self.canvas = Canvas(self.window, width=350, height=250, bg='gray')
        self.canvas.pack()
        self.window.resizable(0, 0)
        self.canvas.create_text(50, 20, text='write your name', anchor=NW, font=(None, 25), fill='#5F1540')
        self.entry = Entry(self.canvas, font=(None, 25), width=17)
        self.entry.place(x=20, y=80)
        self.btn = Button(self.canvas, font=(None, 25), text='save', command=self.click_save)
        self.btn.place(x=130, y=170)
        #self.window.mainloop()

    def click_save(self):
        if len(self.entry.get()) < 1:
            return
        else:
            nickname = self.entry.get()
            self.data.insert_info(nickname, self.level, self.time)
            self.window.destroy()


#object_table = win_table(None, 'beginner', 43)