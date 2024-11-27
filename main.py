from tkinter import *
from pickle import load, dump

# область функций
def set_status():
    pass

def pause_toggle():
    pass

def menu_toggle():
    pass

def key_handler(event):
    if event.keycode == KEY_PLAYER1:
        canvas.move(player1, 100, 0)
    elif event.keycode == KEY_PLAYER2:
        canvas.move(player2, 10, 0)
    elif event.keycode == KEY_S:
        save_game()
    elif event.keycode == KEY_O:
        load_game()

def check_finish():
    pass

def menu_enter():
    pass

def game_new():
    pass

def game_resume():
    pass

def save_game(event):
    x1 = canvas.coords(player1)[0]
    x2 = canvas.coords(player2)[0]
    data = [x1, x2]

    with open ('save.dat', 'wb') as f:
        dump(data, f)
        canvas.itemconfig(text_id, text='СОХРАНЕНО')
def load_game(event):
    global x1, x2
    with open('save.dat', 'rb') as f:
        data = load(f)
        x1,x2 = data
        canvas.coords(player1, x1, y1, x1 + player_size, y1 + player_size)
        canvas.coords(player2, x2, y2, x2 + player_size, y2 + player_size)
        canvas.itemconfig(text_id, text = 'Загружено')

def game_exit():
    pass

def menu_show():
    pass

def menu_hide():
    pass

def menu_up():
    pass

def menu_down():
    pass

def menu_update():
    pass

def menu_create(canvas):
    pass

# область переменных
game_width = 800
game_height = 800
menu_mode = True
menu_options = ['Возврат в игру', 'Новая игра', 'Сохранить', 'Загрузить', 'Выход']
menu_current_index = 3
menu_options_id = []

KEY_UP = 87
KEY_DOWN = 83
KEY_ESC = 27
KEY_ENTER = 13

player_size = 100
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'

x_finish = game_width - 50

KEY_PLAYER1 = 39
KEY_PLAYER2 = 68
KEY_PAUSE = 19
KEY_S = 83
KEY_O = 79

SPEED = 12

game_over = False
pause = False

game_width = 800
game_height = 800

# Окно и объекты
window = Tk()
window.title('DMEC')

canvas = Canvas(window, width=game_width, height=game_height, bg='white')
canvas.pack()
menu_create(canvas)
player1 = canvas.create_rectangle(x1,
                                  y1,
                                  x1 + player_size,
                                  y1 + player_size,
                                  fill=player1_color)
player2 = canvas.create_rectangle(x2,
                                  y2,
                                  x2 + player_size,
                                  y2 + player_size,
                                  fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')

text_id = canvas.create_text(x1,
                             game_height - 400,
                             anchor=SW,
                             font=('Arial', '25'),
                             text='Вперед!')

# Функции обратного вызова
window.bind('<KeyRelease>', key_handler)
window.mainloop()