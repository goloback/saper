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
    def put_and_up_flag(self, value):
        self['text'] = value
        self.print_count_bomb(str(value))
    def print_count_bomb(self, text):
        self.config(text=text)
        str_text = str(text)
        if str_text.isdigit() == True:
            if str_text == '1':
                self.config(fg='red')
            if str_text == '2':
                self.config(fg='blue')
            if str_text == '3':
                self.config(fg='green')
            if str_text == '4':
                self.config(fg='purple')
            if str_text == '5':
                self.config(fg='orange')
            if str_text == '6':
                self.config(fg='yellow')
            if str_text == '7':
                self.config(fg='springgreen')
            if str_text == '8':
                self.config(fg='silver')
        self.config(relief=GROOVE)