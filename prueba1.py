from tkinter import * 

def crearTabla(sopa, x,y):
    n_rows = int(y)
    n_cols = int(x)
    rows = []
    for i in range(n_rows):
        cols = []
        for j in range(n_cols):
            e = Entry(sopa, width=5)
            e.grid(row=i, column=j)
            e.insert(END, '')
            e.config(justify="center")
            cols.append(e)
        rows.append(cols)

def eliminarWidgets(texto1,texto2,n_label1,n_label2, boton):
    texto1.destroy()
    texto2.destroy()
    n_label1.destroy()
    n_label2.destroy()
    boton.destroy()

def pedirFila(raiz, entradas, columnas, filas, lista, palabra_):
    texto = Entry(entradas) #crea un input perteneciente al frame entradas  
    texto.config(justify="center")
    texto.grid(row=0, column=1, padx=10)
    n_label1 = Label(entradas, text="Introduzca la fila correspondiente: ")
    n_label1.grid(row=0, column=0, sticky="e", pady=5, padx=5)
    botonInsertar = Button(entradas, text="Insertar", command=lambda: recuperarLista(raiz, entradas, texto.get(), lista, columnas, filas, palabra_))
    botonInsertar.grid(row=1, column=1, pady=5)
    

def insertarFila(entradas, filaInsertada, lista, columnas, filas):
    if len(filaInsertada)==int(columnas):
        lista.append(filaInsertada.upper())
        mensaje1 = Label(entradas, text="¡Guardado!")
        mensaje1.grid(row=1, column=0, sticky="e", pady=5, padx=5)
    else:
        mensaje2 = Label(entradas, text="¡Reintente!")
        mensaje2.grid(row=1, column=0, sticky="e", pady=5, padx=5)

    return lista


def recuperarLista(raiz, entradas, info, lista, columnas, filas, palabra_):
    global sopa_
    sopa_= insertarFila(entradas, info, lista, columnas, filas)
    if len(sopa_)==int(columnas):
        entradas.destroy()
        entrada2 = Frame(raiz)
        entrada2.grid()
        pedirPalabra(raiz, entrada2, palabra_)

def pedirPalabra(raiz, entrada, palabra_):
    instruccion = Label(entrada, text="Inserte La palabra a buscar")
    instruccion.grid(row=0, column=0, sticky="n", pady=5, padx=5)
    palabra = Entry(entrada)
    palabra.grid(row=1, column=0, sticky="n", pady=5, padx=5)
    agregar = Button(entrada, text="Agregar palabra", command=lambda:recuperarPalabra(entrada, palabra.get(), palabra_))
    agregar.grid(row=2, column=0)
    solucionar = Button(entrada, text="¡Solucionar!", command=lambda:solucionFinal(raiz))
    solucionar.grid(row=2, column=1)

def recuperarPalabra(entrada, palabra, buscar):
    global palabraBuscar
    palabraBuscar = buscar
    if palabra != '':
        buscar.append(palabra.upper())
        guardado = Label(entrada, text="¡Palabra guardada!")
        guardado.grid(row=3, column=0) 
    else:
        error = Label(entrada, text="¡Error! Ingrese una palabra")
        error.grid(row=3, column=0) 

def solucionFinal(raiz):
    raiz.destroy()

def ejecucion(raiz, inicio, inicio1, boton1):
    inicio.destroy()
    inicio1.destroy()
    boton1.destroy()
    
    entradas = Frame(raiz) #Constructor hace el frame
    entradas.grid(row=0,column=1) #empaqueta el frame en la raiz
    entradas.config(width="450", height="350") #Tamaño
    entradas.config(bg="black")#color de fondo

    input_col = Entry(entradas) #crea un input perteneciente al frame entradas  
    input_col.grid(row=0, column=1, padx=10)
    input_col.config(justify="center")
    label_col = Label(entradas, text="Numero de columnas: ")
    label_col.grid(row=0, column=0, sticky="e", pady=5, padx=5)

    input_fil = Entry(entradas) #crea un input perteneciente al frame entradas  
    input_fil.grid(row=1, column=1, padx=10)
    input_fil.config(justify="center")
    label_fil = Label(entradas, text="Numero de filas: ")
    label_fil.grid(row=1, column=0, sticky="e", pady=5, padx=5)

    lista=[]
    palabra_=[]

    boton = Button(entradas, text="Enviar", command=lambda:[pedirFila(raiz, entradas, input_col.get(), input_fil.get(), lista, palabra_), eliminarWidgets(input_col,input_fil,label_col,label_fil, boton)])
    boton.grid(row=2, column=1, pady=5)

#--------Main------------
def main():
    raiz = Tk()
    inicio = Label(raiz, text="BIENVENIDOS AL DESENSOPADOR")
    inicio.grid(row=0,column=0)
    inicio1 = Label(raiz, text="Realizado por: Leonardo Luengas, Juan Andres Castro y Juan Felipe Guerrero")
    inicio1.grid(row=1,column=0)
    boton = Button(raiz, text="INICIAR", command=lambda:ejecucion(raiz, inicio, inicio1, boton))
    boton.grid(row=2, column=0, pady=5)
    raiz.mainloop()