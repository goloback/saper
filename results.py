from tkinter import *
class Results():
    def __init__(self, place, nickname, time, main_canvas):
        self.canvas = Canvas(main_canvas, width=main_canvas['width'], height=70, bg=main_canvas['bg'])
        self.canvas.create_text(20, 20, text=place, font=(None, 25), anchor=NW)
        self.canvas.create_text(120, 20, text=nickname, font=(None, 25), anchor=NW)
        self.canvas.create_text(270, 20, text=time, font=(None, 25), anchor=NW)
        if nickname != '':
            self.delete = self.canvas.create_text(370, 10, text='x', font=(None, 32), anchor=NW, fill='red')
        else:
            self.delete = self.canvas.create_text(370, 10, text='', font=(None, 32), anchor=NW, fill='red')
        self.canvas.place(x=0, y=80*place-10*(place-1))
