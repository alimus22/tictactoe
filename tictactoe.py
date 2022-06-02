"""
Implementation of a simple tic-tac-toe game 

By @Ali Hanni
"""

import tkinter as tk

# Constants
W_HEIGHT = 500
W_WIDTH = 500
W_DIMENSIONS = '500x500'
BG_COLOR = 'white'
FONT = ('Helvetica', 20)

root = tk.Tk()
root.title('Tic Tac Toe')
root.iconbitmap('~/GitHub/tictactoe/img/Tic_tac_toe.xbm')
root.resizable(False, False)
# root.geometry(W_DIMENSIONS)


def clicked(b):
    pass


b1 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b2 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b3 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b4 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b5 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b6 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b7 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b8 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))
b9 = tk.Button(root, bg=BG_COLOR, font=FONT, text=' ', height=3,
               width=6, highlightthickness=0, command=lambda: clicked(b1))

b1.grid(row=0, column=0, sticky='NSEW')
b2.grid(row=0, column=1, sticky='NSEW')
b3.grid(row=0, column=2, sticky='NSEW')
b4.grid(row=1, column=0, sticky='NSEW')
b5.grid(row=1, column=1, sticky='NSEW')
b6.grid(row=1, column=2, sticky='NSEW')
b7.grid(row=2, column=0, sticky='NSEW')
b8.grid(row=2, column=1, sticky='NSEW')
b9.grid(row=2, column=2, sticky='NSEW')

root.mainloop()
