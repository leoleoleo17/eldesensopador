from tkinter import*

#FUNNCIONES--------------------------------
#Primera Pantalla (Pedir columnas y filas)
def ejecucion(raiz, inicio): #pide numero de columnas y de filas, depués llama la funcion pedirFila
    inicio.destroy() #destruye el frame de bienvenida
    
    entradas = Frame(raiz) #Constructor hace el nuevo frame
    entradas.grid(row=0,column=1) #empaqueta el frame en la raiz
    entradas.config(bg="white")

    inputCol = Entry(entradas) #crea una entrada para que el usuario escriba el numero de columnas 
    inputCol.grid(row=0, column=1, padx=10)
    inputCol.config(justify="center")

    labelCol = Label(entradas, text="Número de columnas: ") #crea un label de instruccion para el numero de columnas
    labelCol.grid(row=0, column=0, sticky="e", pady=5, padx=5)
    labelCol.config(bg="white")


    inputFil = Entry(entradas) #crea un input para que el usuario escriba el numero de filas  
    inputFil.grid(row=1, column=1, padx=10)
    inputFil.config(justify="center")

    labelFil = Label(entradas, text="Número de filas: ")#crea un label de instruccion para el numero de filas 
    labelFil.grid(row=1, column=0, sticky="e", pady=5, padx=5)
    labelFil.config(bg="white", border=1, borderwidth=1)

    botonEnviar = Button(entradas, text="Enviar", command=lambda:[pedirFila(raiz, entradas, inputCol.get(), inputFil.get())])
    botonEnviar.grid(row=2, column=1, pady=5)

def pedirFila(raiz, entradas, columnas, filas): #pide el string de letras de cada fila de la sopa de letras y llama a la funcion recuperarLista(principalmente)
    listaSopa = [] #crea una lista vacía que todavía no se usa
    listaPalabras = [] #crea una lista donde entrará el string que el usuario introduzca
    entradas.destroy() #destruye el frame anterior para crear uno nuevo
#Segunda pantalla (Pedir fila o mandar error)
    secondFrame = Frame(raiz)
    secondFrame.grid(row=0,column=1) 
    secondFrame.config(bg="white")
    try: #revisa que lo que introduce ni el numero de columnas ni el de filas sea vacio, una letra o menor a 0 
        if (columnas != '') and (filas !=''): 
            if (int(columnas)>0) and (int(filas)>0):#Si cumple con las condiciones, le pide al usuario introducir la fila
                texto = Entry(secondFrame)
                texto.config(justify="center")
                texto.grid(row=0, column=1, padx=10)
                n_label1 = Label(secondFrame, text="Introduzca la fila correspondiente: ")
                n_label1.grid(row=0, column=0, sticky="e", pady=5, padx=5)
                n_label1.config(bg="white")
                mensaje2 = Label(secondFrame, text='')
                botonInsertar = Button(secondFrame, text="Insertar", padx= 5, command=lambda: [recuperarLista(raiz, secondFrame, texto.get(), listaSopa, columnas, filas, listaPalabras, mensaje2), texto.delete(0,'end')]) #al oprimir el boton llama la funcion y elimina el texto que escribe el usuario en el Entry
                botonInsertar.grid(row=1, column=2, pady=5, padx= 5)
                botonAtras = Button(secondFrame, text="Volver", command=lambda:ejecucion(raiz, secondFrame))#Boton para volver al menu anterior ejecutando la funcion anterior
                botonAtras.grid(row=1,column=0, pady=5)
                botonDelete = Button(secondFrame, text="Eliminar", command=lambda:eliminarDeLista(listaSopa, "¡Fila eliminada con exito!", "No hay filas agregadas", mensaje2))#boton para eliminar la ultima fila agregada 
                botonDelete.grid(row=1,column=1, pady=5, padx= 5)
            else: #si es menor a 0 entra aquí
                n_label1 = Label(secondFrame, text="¡Error! Introduzca un número positivo")
                n_label1.config(bg="white")
                n_label1.grid()
                botonOK = Button(secondFrame, text="¡OK!", command=lambda:ejecucion(raiz, secondFrame))
                botonOK.grid(pady=5)
        else: #Si es vacio entra aquí
            n_label1 = Label(secondFrame, text="¡Error! Introduzca un número")
            n_label1.config(bg="white")
            n_label1.grid()
            n_label1.config(bg="white")
            botonOK = Button(secondFrame, text="¡OK!", command=lambda:ejecucion(raiz, secondFrame))
            botonOK.grid(pady=5)
    except ValueError: #Si no es numero entra aqui
        n_label1 = Label(secondFrame, text="¡Error! Introduzca un número")
        n_label1.grid()
        n_label1.config(bg="white")
        botonOK = Button(secondFrame, text="¡OK!", command=lambda:ejecucion(raiz, secondFrame))
        botonOK.grid(pady=5)

def eliminarDeLista(lista, mensaje1, mensaje2, label_borrar):  
    try:
        lista.pop()
        notificacion = Tk()
        notificacion.title("Aviso")
        notificacion.config(bg="white")
        notificacion.eval('tk::PlaceWindow . center')
        aviso = Label(notificacion, text=mensaje1, font=("Sans Serif",15))
        aviso.grid()
        aviso.config(bg="white")
        boton = Button(notificacion, text="¡OK!", command=lambda:notificacion.destroy())
        boton.grid()
        try:
            label_borrar.config(text = lista[-1])
        except IndexError:
            label_borrar.config(text="")
    
        notificacion.mainloop()
    except IndexError:
        notificacion = Tk()
        notificacion.title("Aviso")
        notificacion.config(bg="white")
        notificacion.eval('tk::PlaceWindow . center')
        aviso = Label(notificacion, text=mensaje2, font=("Sans Serif",15))
        aviso.grid()
        aviso.config(bg="white")
        boton = Button(notificacion, text="¡OK!", command=lambda:notificacion.destroy())
        boton.grid()
        notificacion.mainloop()

def recuperarLista(raiz, frame, info, lista, columnas, filas, listaPalabras, mensaje2):
    global sopa #crea una variable global donde se guardara la lista para poder sacarla de la funcion
    sopa= insertarFila(frame, info, lista, columnas, mensaje2) #la funcion retorna la lista
    if len(sopa)==int(filas): #si se pidieron nFilas veces las filas, la sopa de letras esta completa
        frame.destroy()
        entrada2 = Frame(raiz)
        entrada2.grid(row=0,column=1)
        entrada2.config(bg="white")
        pedirPalabra(raiz, entrada2, listaPalabras) #llama la funcion que empieza a pedir las palabras que hay que buscar

def insertarFila(frame, filaInsertada, lista, columnas, mensaje2): #inserta la fila agregada por el usuario en la lista y despues la retorna
    for x in filaInsertada: #Evita que se guarden palabras que contengan símbolos diferentes a letras
        try:
            int(x)
            mensaje2.config(text="Formato Incorrecto")
            mensaje2.config(bg= "white") #manda el mensaje reintentar
            mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5)
            return []
        except ValueError:
            if x.upper() in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                continue
            else:
                mensaje2.config(text="Formato Incorrecto")
                mensaje2.config(bg= "white") #manda el mensaje reintentar
                mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5)
                return []

    if len(filaInsertada)==int(columnas): #si la cantidad de letras del string que agrega el usuario es igual al de las columnas, entra
        lista.append(filaInsertada.upper()) #la lista recibe la fila insertada en mayusculas porque solo así funciona GUI2
        mensaje1 = Label(frame, text="Última fila guardada:")
        mensaje1.grid(row=2, column=0, sticky="e", pady=5, padx=5)  
        mensaje1.config(bg="white")
        mensaje2.config(text= filaInsertada.upper())
        mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5) #notifica al usuario sobre la ultima fila guardada
        mensaje2.config(bg="white")
    else: #si la cantidad de letras no es la misma, la sopa de letras no estaría completa, por eso mandaría el mensaje
        mensaje2.config(text="Formato Incorrecto") #manda el mensaje reintentar
        mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5)

    return lista
#Tercera pantalla (pedir las palabras)
def pedirPalabra(raiz, frame, listaPalabras): #crea la interfaz para pedir al usuario las palabras que tiene que buscar el programa
    instruccion = Label(frame, text="Inserte la palabra que desea buscar:")
    instruccion.grid(row=0, column=0, sticky="n", pady=5, padx=5)
    instruccion.config(bg="white")
    palabra = Entry(frame)
    palabra.grid(row=0, column=1, sticky="n", pady=5, padx=5)
    text_palabra = palabra.get()
    ultimaPalabra = Label(frame, text= text_palabra.upper())
    agregar = Button(frame, text="Agregar palabra", command=lambda:[recuperarPalabra(palabra.get(), listaPalabras, frame, ultimaPalabra), palabra.delete(0,'end')]) #al oprimir, llama la funcino recuperarPalabra y elimina el texto del entry
    agregar.grid(row=0, column=2, padx= 5,)
    solucionar = Button(frame, text="Solucionar", command=lambda:solucionFinal(raiz, listaPalabras)) #Destruye la raiz para empezar GUI2 segun el main principal
    solucionar.grid(row=1, column=2)
    eliminarPalabra = Button(frame, text="Eliminar palabra", command=lambda:eliminarDeLista(listaPalabras, "¡Palabra eliminada con exito!", "No hay palabras guardadas", ultimaPalabra)) #Destruye la raiz para empezar GUI2 segun el main principal
    eliminarPalabra.grid(row=1, column=1, padx= 5)


def recuperarPalabra(palabra, listaPalabras, frame, mensaje2):
    global palabraBuscar
    palabraBuscar = listaPalabras
    for x in palabra: #Evita que se guarden palabras que contengan símbolos diferentes a letras
        try:
            int(x)
            mensaje2.config(text="Formato Incorrecto")
            mensaje2.config(bg= "white") #manda el mensaje reintentar
            mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5)
            return []
        except ValueError:
            if x.upper() in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                continue
            else:
                mensaje2.config(text="Formato Incorrecto")
                mensaje2.config(bg= "white") #manda el mensaje reintentar
                mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5)
                return []

    if palabra != '':
        palabraBuscar.append(palabra.upper())
        mensaje1 = Label(frame, text="Última palabra guardada:")
        mensaje1.grid(row=2, column=0, sticky="e", pady=5, padx=5)
        mensaje1.config(bg="white")
        mensaje2.config(bg="white", text=palabra.upper())
        mensaje2.grid(row=2, column=1, sticky="e", pady=5, padx=5)

    else:
        mensaje1 = Label(frame, text="¡Error! Ingrese una palabra")
        mensaje1.grid(row=2, column=0, sticky="e", pady=5, padx=5)
        mensaje1.config(bg="white")

def solucionFinal(raiz, listaPalabras):
    if listaPalabras!='':
        raiz.destroy()
    else:
        notificacion = Tk()
        notificacion.title("Aviso")
        notificacion.config(bg="white")
        aviso = Label(notificacion, text="No ha ingresado ninguna palabra", font=("Sans Serif",15))
        aviso.grid()
        aviso.config(bg="white")
        boton = Button(notificacion, text="¡OK!", command=lambda:notificacion.destroy())
        boton.grid()
        notificacion.mainloop()

#MAIN------------------------------
def main():
    #crea la raiz, con titulo y color de fondo 
    raiz = Tk()
    raiz.title("EL DESENSOPADOR")
    raiz.config(bg="white")
    raiz.eval('tk::PlaceWindow . center')
    
    #añade imagen del escudo de la universidad insertada en un label(hacen parte de raiz)
    escudo = PhotoImage(file="escudo.png")
    escudo = escudo.subsample(15)
    lbl_esc = Label(raiz, image=escudo)
    lbl_esc.grid(row=0, column=0, padx=10)
    lbl_esc.config(bg="white")
    
    #añade imagen del logo de MACC insertada en un label (hacen parte de raiz)
    logo = PhotoImage(file="logo.png")
    logo = logo.subsample(9)
    lbl_log = Label(raiz, image=logo)
    lbl_log.grid(row=0, padx=10, column=2, pady=15)
    lbl_log.config(bg="white")
    
    #crea el frame de la bienvenida
    inicio = Frame(raiz)
    inicio.grid(row=0,column=1) #empaqueta el frame en la raiz
    inicio.config(bg="white")

    titulo = Label(inicio, text="BIENVENIDOS AL DESENSOPADOR") #empaqueta el label en el frame
    titulo.grid(row=0,column=0, pady=5)
    titulo.config(bg="white", fg="blue", font=("Sans Serif",20))
    subTitulo = Label(inicio, text="Realizado por: Leonardo Luengas, Juan Andres Castro y Juan Felipe Guerrero")
    subTitulo.grid(row=1,column=0, pady=5)
    subTitulo.config(bg="white", font=("Sans Serif", 9))
    boton = Button(inicio, text="INICIAR", command=lambda:ejecucion(raiz, inicio)) #al oprimir llama a la funcion ejecucion
    boton.grid(row=2, column=0, pady=5)
    boton.config(bg="white")
    raiz.mainloop() #mainloop
