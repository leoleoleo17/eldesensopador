import tkinter
from tkinter import ttk

class Tile: #Los objetos tipo Tile van a ser las partes que constituyen la sopa en su forma gráfica
    def __init__(self, x, y, color, wn, letra):
        self.coordenadax = x
        self.coordenaday = y
        self.letra = letra
        self.color = color
        self.frame = ttk.Frame(wn, height= 10, width = 10)
        self.label = ttk.Label(self.frame, text= letra, background = self.color , font = ("Sans Serif", 20), width = 2, anchor= tkinter.CENTER)
        self.label.pack()

class Sopa: #Es una colección de Tiles 
    def __init__(self, sopa):
        self.sopa = sopa
        self.sopa_tiles = []
    def construir(self, wn): #Construye la colección de Tiles
        column_count = 0
        column_iter = 0
        for row_iter in range(len(self.sopa)):
            wn.rowconfigure(row_iter, weight = 1)
            for column_iter in range(len(self.sopa[row_iter])):
                if column_count == 0:
                    wn.columnconfigure(column_iter, weight = 1)
                tile = Tile(row_iter, column_iter, "white",wn, self.sopa[row_iter][column_iter])
                tile.frame.grid(column = column_iter, row = row_iter )
                self.sopa_tiles.append(tile)
            column_count += 1

    def highlight(self, coordenadas, color, palabra, wn): #Esta función resalta las soluciones en la sopa
        self.construir(wn) #Reinicia el color de todas las tiles a blanco
        coordenadas = coordenadas[palabra]
        x_coordenadas = []
        y_coordenadas = []
        if coordenadas == None: #Muestra un error cuando la palabra no está en la sopa
            error = tkinter.Tk()
            error.configure(bg= "white")
            error.title("¡Error!")
            error.eval('tk::PlaceWindow . center')

            notificacion = ttk.Label(error, background="white", font=("Sans Serif", 20), text="La palabra no está en la sopa")
            notificacion.grid(row= 0, column=0)

            boton = ttk.Button(error, text= "OK", command=lambda: error.destroy())
            boton.grid(column= 0, row =1)
            return 0
        for w in range(len(coordenadas)):
            if w % 2 == 0:
                x_coordenadas.append(coordenadas[w])
            else:
                y_coordenadas.append(coordenadas[w])
        for x, y in zip(x_coordenadas,y_coordenadas): #Zip itera ambas listas al mismo tiempo
            for tile in self.sopa_tiles:
                if (tile.coordenadax == x) and (tile.coordenaday == y):
                    tile.frame.destroy()
                    new_tile = Tile(x,y, color , wn, tile.letra)
                    new_tile.frame.grid(column= y, row = x)
            
def main(coordenadas, sopa): #Ejecuta el GUI como tal
    window = tkinter.Tk()
    window.configure(bg="white")
    window.title("¡Haz click en los botones!")
    window.eval('tk::PlaceWindow . center')

    mainframe = tkinter.Frame(window, bg= "white")
    s = Sopa(sopa)
    s.construir(mainframe)
    window.rowconfigure(0,weight=1)
    window.columnconfigure(0,weight=1)
    mainframe.grid(column= 0, row= 0) #Espacio para la sopa en la ventana principal
    
    botones = ttk.Frame(window)
    counter_rows = 0
    for palabra in coordenadas: #Construye los botones a la derecha de la sopa
        b = ttk.Button(botones,text = palabra, command= lambda new_word = palabra: s.highlight(coordenadas, "yellow", new_word, mainframe)) #Crea una función lambda para evitar que se ejecute highlight cuando se crean los botones
        b.grid(row= counter_rows, column=0)
        counter_rows += 1

    window.columnconfigure(1, weight=1) #Espacio para los botones en la ventana principal
    botones.grid(row= 0, column = 1) 
    window.mainloop()