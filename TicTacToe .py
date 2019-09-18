# here we import the library for gui 

from tkinter import *
from tkinter import  messagebox

#here we design the GUI of tic- tac-toe

gui = Tk()
gui.title('TIC-TAC-TOE')
gui.geometry('1100x730')

lb = Label(gui, text = 'Player 1: X', font =('Helvetica', '25'))
lb.grid(row=1, column=0)
lb = Label(gui, text = 'Player 2: O', font =('Helvetica', '25'))
lb.grid(row=2, column=0)

# here we program all buttons

turn = 1
def click1():
    global  turn
    if btn1['text'] == " ":
        if turn == 1:
            btn1['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn1['text'] = 'O'
            turn = 1
        check_winner()
def click2():
    global  turn
    if btn2['text'] == " ":
        if turn == 1:
            btn2['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn2['text'] = 'O'
            turn = 1
        check_winner()
def click3():
    global  turn
    if btn3['text'] == " ":
        if turn == 1:
            btn3['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn3['text'] = 'O'
            turn = 1
        check_winner()
def click4():
    global  turn
    if btn4['text'] == " ":
        if turn == 1:
            btn4['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn4['text'] = 'O'
            turn = 1
        check_winner()
def click5():
    global  turn
    if btn5['text'] == " ":
        if turn == 1:
            btn5['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn5['text'] = 'O'
            turn = 1
        check_winner()
def click6():
    global  turn
    if btn6['text'] == " ":
        if turn == 1:
            btn6['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn6['text'] = 'O'
            turn = 1
        check_winner()
def click7():
    global  turn
    if btn7['text'] == " ":
        if turn == 1:
            btn7['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn7['text'] = 'O'
            turn = 1
        check_winner()
def click8():
    global  turn
    if btn8['text'] == " ":
        if turn == 1:
            btn8['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn8['text'] = 'O'
            turn = 1
        check_winner()
def click9():
    global  turn
    if btn9['text'] == " ":
        if turn == 1:
            btn9['text'] = 'X'
            turn = 2
        elif turn == 2:
            btn9['text'] = 'O'
            turn = 1
        check_winner()


# here we write code to find the winner

loop = 1
def check_winner():
    global loop
    a1 = btn1['text']
    a2 = btn2['text']
    a3 = btn3['text']
    a4 = btn4['text']
    a5 = btn5['text']
    a6 = btn6['text']
    a7 = btn7['text']
    a8 = btn8['text']
    a9 = btn9['text']
    loop = loop+1
    if a1 == a2 and a2 == a3 and a1 =='X' or a1 == a2 and a2 == a3 and a1 =='O':
        win(btn1['text'])
    if a4 == a5 and a5 == a6 and a4 =='X' or a4 == a5 and a5 == a6 and a4 =='O':
        win(btn4['text'])
    if a7 == a8 and a8 == a9 and a7 =='X' or a7 == a8 and a8 == a9 and a7 =='O':
        win(btn7['text'])
    if a1 == a4 and a4 == a7 and a1 =='X' or a1 == a4 and a4 == a7 and a1 =='O':
        win(btn1['text'])
    if a2 == a5 and a5 == a8 and a2 =='X' or a2 == a5 and a5 == a8 and a2 =='O':
        win(btn2['text'])
    if a3 == a6 and a6 == a9 and a3 =='X' or a3 == a6 and a6 == a9 and a3 =='O':
        win(btn3['text'])
    if a3 == a5 and a5 == a7 and a3 =='X' or a3 == a5 and a5 == a7 and a3 =='O':
        win(btn3['text'])
    if a1 == a5 and a5 == a9 and a1 =='X' or a1 == a5 and a5 == a9 and a1 =='O':
        win(btn1['text'])
    if loop == 10:
        info = "match tied: TRY AGAIN :)"
        messagebox.showinfo('TIE', info)
        gui.destroy()

def win(text):
    if text  == 'X':
        result = 'congratulations player {} win'.format(1)
    elif text == "O":
        result = 'congratulations player {} win'.format(2)
    messagebox.showinfo('congratulation', result)
    gui.destroy()


# here we make 9x9 grid

btn1 = Button(gui, text = ' ', bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click1)
btn1.grid(row = 1 , column = 1)
btn2 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click2)
btn2.grid(row = 1 , column = 2)
btn3 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click3)
btn3.grid(row = 1 , column = 3)
btn4 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click4)
btn4.grid(row = 2 , column = 1)
btn5 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click5)
btn5.grid(row = 2 , column = 2)
btn6 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click6)
btn6.grid(row = 2 , column = 3)
btn7 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click7)
btn7.grid(row = 3 , column = 1)
btn8 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click8)
btn8.grid(row = 3 , column = 2)
btn9 = Button(gui, text = ' ',bg = 'light blue', fg = 'black', width = 20 , height = 7, font = ('Helvetica', '20'), command = click9)
btn9.grid(row = 3 , column = 3)

gui.mainloop()