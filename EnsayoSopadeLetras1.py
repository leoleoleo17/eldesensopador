row1 = "BQWQDMF" #Palabras: Casa, Zapato, Dulce, Juancho
row2 = "GKWRUBZ"
row3 = "TOBCLFA"
row4 = "LXTACKP"
row5 = "RCDSELA"
row6 = "ZODAFJT"
row7 = "JUANCHO"
rows = [row1, row2, row3, row4, row5, row6, row7] #Crear una lista con una variable para cada row, segpun un n de rows, automática

def igualpalabra(ltr,wrd, es_primero): #Otro parametro para no escoger una distinta a la primera
#Comenzar con una sola row y considerar todas las posibilidades
    position = 0
    if es_primero == 0:
        for w in [-1,0]:
            if wrd[w] == ltr:
                return w
    else:
        for x in wrd:
            if x == ltr:
                return position
            position += 1
            
def buscapalabras(wrd):
    count = 0
    rowcounter = 0
    countinterno = 0
    while rowcounter <= len(rows):
        for x in rows[countinterno]:
            if count == 0: #Revisa si tiene la primera o última letra para empezar a revisar la palábra completa
                for w in [-1,1]:
                    if x == wrd[w]:
                        count += 1
        countinterno +=1
        rowcounter += 1
                