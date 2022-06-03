"""
Implementation of a simple tic-tac-toe game

By @Ali Hanni
"""

from ast import Global
import tkinter as tk
from tkinter import messagebox

# Constants
W_HEIGHT = 500
W_WIDTH = 500
W_DIMENSIONS = '500x500'
BG_COLOR = 'white'
FONT = ('Helvetica', 20)
player = 1
count = 0
board = {}


def clicked(b):
    global player, count
    if b['text'] == ' ':
        if player == 1:
            b['text'] = 'O'
            player = 2
            count += 1
        elif player == 2:
            b['text'] = 'X'
            player = 1
            count += 1
    else:
        messagebox.showerror('Tic Tac Toe',
                             'Position already played, play another position !')

    if count >= 5:
        checkWin()


def checkWin():
    pass


root = tk.Tk()
root.title('Tic Tac Toe')
root.iconbitmap('~/GitHub/tictactoe/img/Tic_tac_toe.xbm')
root.resizable(False, False)
# root.geometry(W_DIMENSIONS)

b1 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b2 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b2))
b3 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b3))
b4 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b4))
b5 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b5))
b6 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b6))
b7 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b7))
b8 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b8))
b9 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b9))


def generateBoard():
    for x in range(1, 10):
        board['b{0}'.format(x)] = ' '


b1.grid(row=0, column=0, sticky='NSEW')
b2.grid(row=0, column=1, sticky='NSEW')
b3.grid(row=0, column=2, sticky='NSEW')
b4.grid(row=1, column=0, sticky='NSEW')
b5.grid(row=1, column=1, sticky='NSEW')
b6.grid(row=1, column=2, sticky='NSEW')
b7.grid(row=2, column=0, sticky='NSEW')
b8.grid(row=2, column=1, sticky='NSEW')
b9.grid(row=2, column=2, sticky='NSEW')

generateBoard()
print(board)


root.mainloop()
