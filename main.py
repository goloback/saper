from tkinter import *
from sapor_btn import ButtonSapor
from random import randint
from datetime import datetime
import threading
def check_win():
    for btn in btn_list:
        if btn.is_bomb == False and btn.btn_check == False:
            return False
    return True

def bomb_touch():
    for btn in btn_list:
        if btn.is_bomb == True:
            continue
        if btn.index>1 and btn.index<count_cols:
            btn.type = "top"
            btn.index_nearst_btn.append(btn.index-1-1)
            btn.index_nearst_btn.append(btn.index + 1 - 1)
            btn.index_nearst_btn.append(btn.index-1+count_cols-1)
            btn.index_nearst_btn.append(btn.index+count_cols-1)
            btn.index_nearst_btn.append(btn.index + count_cols )
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb+=1
        elif btn.index > count_cols*count_rows-count_cols+1 and btn.index < count_cols*count_rows:
            btn.type = "bottom"
            btn.index_nearst_btn.append(btn.index - 1 - 1)
            btn.index_nearst_btn.append(btn.index + 1 - 1)
            btn.index_nearst_btn.append(btn.index - 1 - count_cols - 1)
            btn.index_nearst_btn.append(btn.index - count_cols - 1)
            btn.index_nearst_btn.append(btn.index - count_cols)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1

        elif btn.index != 1 and btn.index!= count_cols*count_rows-count_cols+1 and btn.index % count_cols == 1:
            btn.type = 'left'
            btn.index_nearst_btn.append(btn.index + 1 - 1)
            btn.index_nearst_btn.append(btn.index- count_cols - 1)
            btn.index_nearst_btn.append(btn.index + 1 - count_cols - 1)
            btn.index_nearst_btn.append(btn.index + count_cols)
            btn.index_nearst_btn.append(btn.index + count_cols - 1)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        elif btn.index != count_cols and btn.index!= count_cols*count_rows and btn.index % count_cols == 0:
            btn.type = 'right'
            btn.index_nearst_btn.append(btn.index - 1 - 1)
            btn.index_nearst_btn.append(btn.index- count_cols - 1)
            btn.index_nearst_btn.append(btn.index - 1 - count_cols - 1)
            btn.index_nearst_btn.append(btn.index + count_cols -1 - 1)
            btn.index_nearst_btn.append(btn.index + count_cols - 1)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        elif btn.index == 1:
            btn.type = 'left_top_corner'
            btn.index_nearst_btn.append(btn.index + 1 - 1)
            btn.index_nearst_btn.append(btn.index+ count_cols - 1)
            btn.index_nearst_btn.append(btn.index + count_cols)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        elif btn.index == count_cols*count_rows-count_cols+1:
            btn.type = 'left_bottom_corner'
            btn.index_nearst_btn.append(btn.index + 1 - 1)
            btn.index_nearst_btn.append(btn.index - count_cols - 1)
            btn.index_nearst_btn.append(btn.index - count_cols)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        elif btn.index == count_cols:
            btn.type = 'right_top_corner'
            btn.index_nearst_btn.append(btn.index - 1 - 1)
            btn.index_nearst_btn.append(btn.index + count_cols - 1)
            btn.index_nearst_btn.append(btn.index + count_cols - 1 - 1)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        elif btn.index == count_cols*count_rows:
            btn.type = 'right_bottom_corner'
            btn.index_nearst_btn.append(btn.index - 1 - 1)
            btn.index_nearst_btn.append(btn.index - count_cols - 1)
            btn.index_nearst_btn.append(btn.index - count_cols - 1 - 1)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        else:
            btn.type == 'center'
            btn.index_nearst_btn.append(btn.index - 1 - 1)
            btn.index_nearst_btn.append(btn.index + 1 - 1)
            btn.index_nearst_btn.append(btn.index- count_cols - 1)
            btn.index_nearst_btn.append(btn.index - 1 - count_cols - 1)
            btn.index_nearst_btn.append(btn.index + count_cols -1 - 1)
            btn.index_nearst_btn.append(btn.index - count_cols)
            btn.index_nearst_btn.append(btn.index + count_cols)
            btn.index_nearst_btn.append(btn.index + count_cols - 1)
            for i in btn.index_nearst_btn:
                if btn_list[i].is_bomb == True:
                    btn.count_touch_bomb += 1
        #btn.show_figure(btn.count_touch_bomb)
def click_left(event):
    global start_game, update_time_click
    if start_game is None:
        start_game = True
        if update_time_click == False:
            update_time()
            update_time_click = True
    if start_game == False:
        return
    index = event.widget.index-1
    btn_list[index].btn_check = True
    if btn_list[index].is_bomb == False:
        btn_list[index].text_print(str(btn_list[index].count_touch_bomb))
    if btn_list[index].count_touch_bomb == 0:
        btn0(index)
    if check_win() == True:
        print('win')
    if btn_list[index].is_bomb == True:
        start_game = False
        for flag in btn_list:
            if flag.is_bomb == True:
                flag.text_print('💣')

def click_right(event):
    global flags_count
    index = event.widget.index-1
    if btn_list[index]['text'] == '':
        btn_list[index]['text']='🚩'
        flags_count += 1
        btn_list[index]['fg'] = 'red'
    else:
        btn_list[index]['text'] = ''
        flags_count -= 1
    canvas.itemconfigure(text_count_bombs, text = bomb_count - flags_count)

def btn0(index):
    for i in btn_list[index].index_nearst_btn:
        if btn_list[i].btn_check == True:
            continue
        btn_list[i].show_figure(btn_list[i].count_touch_bomb)
        btn_list[i].btn_check = True
        if btn_list[i].count_touch_bomb == 0 and btn_list[i].is_bomb == False:
            btn_list[i].show_figure(0)
            btn0(i)

def create_bomb():
    while len(bomb_list)<bomb_count:
        bomb = randint(1, count_rows*count_cols)
        if bomb in bomb_list:
            continue
        bomb_list.append(bomb)

def apply_bomb():
    for btn in btn_list:
        if btn.index in bomb_list:
            btn.is_bomb = True

def click_beginner():
    global count_rows, count_cols, bomb_count
    count_rows = 9
    count_cols = 9
    bomb_count = 10
    create_gameplay()

def click_intermediate():
    global count_rows, count_cols, bomb_count
    count_rows = 16
    count_cols = 16
    bomb_count = 40
    create_gameplay()

def click_expert():
    global count_rows, count_cols, bomb_count
    count_rows = 20
    count_cols = 18
    bomb_count = 99
    create_gameplay()

def create_gameplay():
    global start_game, flags_count, game_time
    game_time = 0
    canvas.itemconfigure(timer, text=0)
    start_game = None
    flags_count = 0
    canvas.config(width=count_cols*45)
    canvas.grid(row=1, column=0, columnspan=count_cols)
    canvas.itemconfigure(text_count_bombs, text=bomb_count)
    for btn in btn_list:
        btn.destroy()
    btn_list.clear()
    bomb_list.clear()
    index = 1
    for row in range(count_rows):
        for col in range(count_cols):
            btn = ButtonSapor(window, width=5, height=2)
            btn.grid(row=row + 2, column=col)
            btn.index = index
            index += 1
            btn.bind('<ButtonRelease-1>', click_left)
            btn.bind('<Button-3>', click_right)
            btn_list.append(btn)
    create_bomb()
    apply_bomb()
    bomb_touch()

def update_time():
    global game_time
    if start_game == True:
        canvas.itemconfigure(timer, text=game_time)
        game_time += 1
    window.after(1000, update_time)


update_time_click = False
start_game = None
window = Tk()
count_rows = 12
count_cols = 12
bomb_count = count_cols*count_rows//12
flags_count = 0
game_time = 0
current_time = datetime.now().second
canvas = Canvas(window, width=count_cols*45, height=50, bg='#5F1540')
canvas.grid(row=1, column=0, columnspan=count_cols)
text_count_bombs = canvas.create_text(5, 5, anchor=NW, text=bomb_count, fill='#cd0000', font=(None, 25))
beginner = Button(canvas, bg='grey', fg='white', font=(None, 15), text='beginner', command=click_beginner)
beginner.place(x=45, y=7)
Intermediate = Button(canvas, bg='grey', fg='white', font=(None, 15), text='Intermediate', command=click_intermediate)
Intermediate.place(x=140, y=7)
expert = Button(canvas, bg='grey', fg='white', font=(None, 15), text='expert', command=click_expert)
expert.place(x=270, y=7)
timer = canvas.create_text(360, 5, anchor=NW, text='00', fill='#cd0000', font=(None, 25))
btn_list = []
bomb_list = []
click_beginner()

thread = threading.Thread(target=timer)
thread.start()
window.mainloop()