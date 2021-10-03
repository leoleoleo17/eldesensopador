def primeraletra(wrd, row, listadepalabras, index_abs): #Busca las instancias donde está la letra dentro de la sopa, devuelve una lista con los indices
    indices = [] #Lista de indices donde se ubica la letra de la palabra que buscamos
    errornone = 0 #Evita error de desempacar None como una tupla de longitud 2
    indice_lista = 0
    for w in listadepalabras[row]:
        if wrd[index_abs] == w:
            errornone += 1
            indices.append(indice_lista)
        indice_lista += 1
    if errornone == 0:
        return (None, errornone)
    return (indices, index_abs)
            
def derecha(row, position, listadepalabras, wrd_og, wrd_comparar): #Busca a la derecha de la letra (Misma fila)
    coordenadas = ()
    for w in range(len(wrd_og)):
        wrd_comparar += listadepalabras[row][position + w]
    if wrd_comparar == wrd_og:
        for x in wrd_comparar:
            coordenadas += (row, position)
            position += 1
        return coordenadas
        
def abajo(row, position, listadepalabras, wrd_og, wrd_comparar): #Busca la palabra abajo de la letra (misma columna) 
    coordenadas = ()
    for w in range(len(wrd_og)):
        wrd_comparar += listadepalabras[row+w][position]
    if wrd_comparar == wrd_og:
        for x in wrd_comparar:
            coordenadas += (row, position)
            row += 1
        return coordenadas
        
def diagonal(row, position, listadepalabras, wrd_og, wrd_comparar): #Busca la palabra en diagonal de izquierda a derecha
    coordenadas = ()
    for w in range(len(wrd_og)):
        wrd_comparar += listadepalabras[row + w][position + w]
    if wrd_comparar == wrd_og:
        for x in wrd_comparar:
            coordenadas += (row, position)
            position += 1
            row += 1
        return coordenadas  
    
def diagonal_al_reves(row, position, listadepalabras, wrd_og, wrd_comparar): #Busca la palabra en la diagonal invertida de derecha a izquierda
    coordenadas = ()
    for w in range(len(wrd_og)):
        wrd_comparar += listadepalabras[row + w][position - w]
    if wrd_comparar == wrd_og:
        for x in wrd_comparar:
            coordenadas += (row, position)
            position -= 1
            row += 1
        return coordenadas 
    
def palabras_invertidas(row, position, listadepalabras, wrd):
    palabratemp = "" #Reescribe la palabra que buscamos al revés
    palabratemp2 = "" #Palabra extraída de la sopa de letras para comparar
    for x in range(1,(len(wrd)+1)):
        palabratemp += wrd[(-1)*x]
    if (position + len(wrd)) <= (len(listadepalabras[row])): #Revisa si la palabra cabe a la derecha
        coordenadas= derecha(row, position, listadepalabras, palabratemp, palabratemp2)
        if coordenadas != None:
            return coordenadas
    if (row + len(wrd)) <= (len(listadepalabras)): #Revisa si la palabra cabe hacia abajo
        coordenadas = abajo(row, position, listadepalabras, palabratemp, palabratemp2)
        if coordenadas != None:
            return coordenadas
    if ((position + len(wrd)) <= (len(listadepalabras[row]))) and ((row + len(wrd)) <= (len(listadepalabras))): #Revisa si la palabra cabe en diagonal
        coordenadas = diagonal(row, position, listadepalabras, palabratemp, palabratemp2)
        if coordenadas != None:
            return coordenadas
    if ((len(wrd)-position) <= (len(listadepalabras[row]))) and ((row + len(wrd)) <= (len(listadepalabras))): #Revisa si la palabra cabe en diagonal de derecha a izquierda
        coordenadas = diagonal_al_reves(row, position, listadepalabras, palabratemp, palabratemp2)
        if coordenadas != None:
            return coordenadas
            
def palabras_al_derecho(row, position, listadepalabras, wrd): 
    palabratemp2 = ""
    if (position + len(wrd)) <= (len(listadepalabras[row])): #Revisa si la palabra cabe a la derecha 
        coordenadas= derecha(row, position, listadepalabras, wrd, palabratemp2)
        if coordenadas != None:
            return coordenadas
    if (row + len(wrd)) <= (len(listadepalabras)): #Revisa si la palabra cabe hacia abajo
        coordenadas = abajo(row, position, listadepalabras, wrd, palabratemp2)
        if coordenadas != None:
            return coordenadas
    if ((position + len(wrd)) <= (len(listadepalabras[row]))) and ((row + len(wrd)) <= (len(listadepalabras))): #Revisa si la palabra cabe en diagonal
        coordenadas = diagonal(row, position, listadepalabras, wrd, palabratemp2)
        if coordenadas != None:
            return coordenadas
    if ((len(wrd)-position) <= (len(listadepalabras[row]))) and ((row + len(wrd)) <= (len(listadepalabras))): #Revisa si la palabra cabe en diagonal de derecha a izquierda
        coordenadas = diagonal_al_reves(row, position, listadepalabras, wrd, palabratemp2)
        if coordenadas != None:
            return coordenadas
  
def buscaalrededor(row, indices, listadepalabras, wrd, index):
    coordenadas = ()
    #Construye la palabra y la compara en las direcciones posibles (las otras direcciones son redundantes) 
    for position in indices: #Itera la lista de índices para pasar por todas las posibilidades para un valor dado de indice_abs
        if index == -1:
            coordenadas = palabras_invertidas(row, position, listadepalabras, wrd)
            if coordenadas == None:
                continue
            else:
                return coordenadas
        elif index == 0:
            coordenadas = palabras_al_derecho(row, position, listadepalabras, wrd)
            if coordenadas == None:
                continue
            else:
                return coordenadas
                
def buscapalabras(wrd, listadepalabras):
    rowcounter = 0
    while rowcounter < len(listadepalabras):
        indice_abs = -1 #Puede tomar valores -1 o 0, es el índice para la primera o la última letra
        (indices, index) = primeraletra(wrd, rowcounter, listadepalabras, indice_abs)
        if (indices == None): 
                indice_abs = 0
                (indices, index) = primeraletra(wrd, rowcounter, listadepalabras, indice_abs)
                if indices == None:
                    rowcounter +=1
                    continue
        coordenadas = buscaalrededor(rowcounter, indices, listadepalabras, wrd, index)
        if coordenadas == None: 
            if indice_abs == -1: #Puede que al tomar valor -1 primero, se haya saltado la posibilidad de que la palabra se encuentre con el índice 0
                indice_abs = 0
                (indices, index) = primeraletra(wrd, rowcounter, listadepalabras, indice_abs)
                if (indices == None):
                    rowcounter += 1
                    continue
                coordenadas = buscaalrededor(rowcounter, indices, listadepalabras, wrd, index) 
                if (coordenadas == None):
                    rowcounter += 1
                    continue
            else:
                rowcounter += 1
                continue
        return coordenadas