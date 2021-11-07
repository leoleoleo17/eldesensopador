import tkinter
from tkinter import ttk

class Tile: #Los objetos tipo Tile van a ser las partes que constituyen la sopa en su forma gráfica
    def __init__(self, x, y, color, wn, letra):
        self.coordenadax = x
        self.coordenaday = y
        self.color = color
        self.frame = ttk.Frame(wn, borderwidth = 1)
        self.label = ttk.Label(self.frame, text= letra, background = "white", font = ("Sans Serif",20),)
        self.label.pack()
class Sopa:
    def __init__(self, sopa):
        self.sopa = sopa
        self.sopa_tiles = []
    def construir(self, wn):
        column_count = 0
        for row_iter in range(len(self.sopa)):
            wn.rowconfigure(row_iter, weight = 1)
            for column_iter in range(len(self.sopa[row_iter])):
                if column_count == 0:
                    wn.columnconfigure(column_iter, weight = 1)
                tile = Tile(row_iter, column_iter, "white",wn, self.sopa[row_iter][column_iter])
                tile.frame.grid(column = column_iter, row = row_iter )
                self.sopa_tiles.append(tile)
            column_count += 1
    def highlight(self, coordenadas):
        pass

def main(coordenadas, sopa):
    window = tkinter.Tk()
    frm = tkinter.Frame(window, bg = "white")
    s = Sopa(sopa)
    s.construir(frm)
    frm.rowconfigure(0, weight =1)
    frm.columnconfigure(0, weight =1)
    frm.grid()
    window.mainloop()
    
