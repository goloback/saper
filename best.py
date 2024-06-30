from tkinter import *
from results import Results
class players_results():
    def __init__(self, level, data_base):
        self.level = level
        self.data_base = data_base
        self.players=self.data_base.get_players_level(level)
        self.add_empty_result()
        self.create_window()
        print(self.players)

    def add_empty_result(self):
        while len(self.players) < 5:
            empty_res = ('', '', '', '')
            self.players.append(empty_res)


    def create_window(self):
        self.window = Tk()
        self.window.title('the best')
        self.canvas = Canvas(self.window, width=34*12, height=430, bg='gray')
        self.canvas.pack()
        self.window.resizable(0, 0)
        x = 70
        if self.level == 'expert':
            x = 130
        elif self.level == 'beginner':
            x = 100
        self.canvas.create_text(x, 20, text=self.level, anchor=NW, font=(None, 35), fill='#5F1540')
        self.create_res()
    def create_res(self):
        self.row_1 = Results(1, self.players[0][1], self.players[0][3], self.canvas)
        self.row_1.canvas.tag_bind(self.row_1.delete, '<Button-1>', lambda event: self.delete(self.players[0][0]))
        self.row_2 = Results(2, self.players[1][1], self.players[1][3], self.canvas)
        self.row_2.canvas.tag_bind(self.row_2.delete, '<Button-1>', lambda event: self.delete(self.players[1][0]))
        self.row_3 = Results(3, self.players[2][1], self.players[2][3], self.canvas)
        self.row_3.canvas.tag_bind(self.row_3.delete, '<Button-1>', lambda event: self.delete(self.players[2][0]))
        self.row_4 = Results(4, self.players[3][1], self.players[3][3], self.canvas)
        self.row_4.canvas.tag_bind(self.row_4.delete, '<Button-1>', lambda event: self.delete(self.players[3][0]))
        self.row_5 = Results(5, self.players[4][1], self.players[4][3], self.canvas)
        self.row_5.canvas.tag_bind(self.row_5.delete, '<Button-1>', lambda event: self.delete(self.players[4][0]))

    def delete(self, id):
        self.data_base.delete_info(id)
        self.players = self.data_base.get_players_level(self.level)
        self.add_empty_result()
        self.create_res()



