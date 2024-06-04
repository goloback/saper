from tkinter import *

class ButtonSapor(Button):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=None, cnf={}, **kw)
        self.is_bomb = False
        self.index = -1
        self.type = 'center'
        self.index_nearst_btn = []
        self.count_touch_bomb = 0
        self.btn_check = False
    def show_figure(self, value):
        self['text'] = value
        self.text_print(str(value))
        self.config(relief=SUNKEN)
    def text_print(self, text):
        self.config(text=text)
        if text.isdigit() == True:
            if text == '1':
                self.config(fg='red')
            if text == '2':
                self.config(fg='blue')
            if text == '3':
                self.config(fg='green')
            if text == '4':
                self.config(fg='purple')
            if text == '5':
                self.config(fg='orange')
            if text == '6':
                self.config(fg='yellow')
            if text == '7':
                self.config(fg='springgreen')
            if text == '8':
                self.config(fg='silver')
        self.config(relief=SUNKEN)