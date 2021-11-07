import funciones
import GUI2

row1 = "BQWQDMF" 
row2 = "GKZRUBZ"
row3 = "TOBCLFA"
row4 = "LXTACKP"
row5 = "RCDSELA"
row6 = "ZODAFJT"
row7 = "JUANCHO"
sopa = (row1, row2, row3, row4, row5, row6, row7)
coordenadas_dict = {}

words = ("CASA", "JUANCHO", "ZAPATO", "DULCE")
for x in words:
    coordenadas = ()
    coordenadas = funciones.buscapalabras(x, sopa)
    coordenadas_dict[x]= coordenadas
    print("La palabra {0} se encuentra en: ".format(x), coordenadas)
    
GUI2.main(coordenadas_dict, sopa)