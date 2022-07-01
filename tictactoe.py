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


class Tictactoe:
    def __init__(self):
        self.board = [[' ' for x in range(3)] for y in range(3)]

    def generateBoard(self):
        for x in range(2):
            for y in range(2):
                self.board[x][y] = ' '

    def clicked(self, b, x, y):
        global player, count
        if b['text'] == ' ':
            if player == 1:
                b['text'] = 'O'
                player = 2
                count += 1
                self.board[y][x] = 'O'
                self.checkWin(x, y, 'O')
            elif player == 2:
                b['text'] = 'X'
                player = 1
                count += 1
                self.board[y][x] = 'X'
                self.checkWin(x, y, 'X')
        else:
            messagebox.showerror('Tic Tac Toe',
                                 'Position already played, play another position !')

    def checkWin(self, x, y, state):
        self.check_col(x, state)
        self.check_rows(y, state)
        self.check_diagonal(state)                
    
    def check_col(self, x, state):
        for i in range(3):
            if self.board[i][x] != state:
                break
            elif i == 2:
                if state == 'O':
                    messagebox.showinfo(
                        'YOU WIN', 'Congratulations you won !')
                    return
                elif state == 'X':
                    messagebox.showinfo(
                        'COMPUTER WIN', 'Computer won !')
                    return

    
    def check_rows(self, y, state):
        for i in range(3):
            if self.board[y][i] != state:
                break
            elif i == 2:
                if state == 'O':
                    messagebox.showinfo(
                        'YOU WIN', 'Congratulations you won !')
                    return
                elif state == 'X':
                    messagebox.showinfo(
                        'COMPUTER WIN', 'Computer won !')
                    return


    def check_diagonal(self, state):
        won = 0

        for i in range(3):
            if self.board[0 + i][0 + i] != state:
                won += 1
                break
        if won == 1:
            for i in range(3):
                print('(', 2- i, ', ', 0 + i, ')')
                if self.board[2 - i][0 + i] != state:
                    won += 1
                    return
        print('won:', won)
        if won < 2:
            if state == 'O':
                messagebox.showinfo(
                    'YOU WIN', 'Congratulations you won !')
                return
            elif state == 'X':
                messagebox.showinfo(
                    'COMPUTER WIN', 'Computer won !')
                return

class Application:
    def __init__(self, ):
        tictactoe = Tictactoe()
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')
        self.root.iconbitmap('~/GitHub/tictactoe/img/Tic_tac_toe.xbm')
        self.root.resizable(False, False)
        # self.root.geometry(W_DIMENSIONS)

        b1 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b1, 0, 0))
        b2 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b2, 1, 0))
        b3 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b3, 2, 0))
        b4 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b4, 0, 1))
        b5 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b5, 1, 1))
        b6 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b6, 2, 1))
        b7 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b7, 0, 2))
        b8 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b8, 1, 2))
        b9 = tk.Button(self.root, bg=BG_COLOR, font=FONT, text=' ', height=3,
                       width=6, highlightthickness=0, command=lambda: tictactoe.clicked(b9, 2, 2))

        b1.grid(row=0, column=0, sticky='NSEW')
        b2.grid(row=0, column=1, sticky='NSEW')
        b3.grid(row=0, column=2, sticky='NSEW')
        b4.grid(row=1, column=0, sticky='NSEW')
        b5.grid(row=1, column=1, sticky='NSEW')
        b6.grid(row=1, column=2, sticky='NSEW')
        b7.grid(row=2, column=0, sticky='NSEW')
        b8.grid(row=2, column=1, sticky='NSEW')
        b9.grid(row=2, column=2, sticky='NSEW')

        self.root.mainloop()


app = Application()
