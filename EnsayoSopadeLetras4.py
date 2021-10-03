import funciones

row1 = "BQWQDMF" 
row2 = "GKZRUBZ"
row3 = "TOBCLFA"
row4 = "LXTACKP"
row5 = "RCDSELA"
row6 = "ZODAFJT"
row7 = "JUANCHO"
rows = (row1, row2, row3, row4, row5, row6, row7)

words = ("CASA", "JUANCHO", "ZAPATO", "DULCE")
for x in words:
    coordenadas = ()
    coordenadas = funciones.buscapalabras(x, rows)
    print("La palabra {0} se encuentra en: ".format(x), coordenadas)
                