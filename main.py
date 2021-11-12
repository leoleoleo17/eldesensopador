import algoritmo
import GUI2
import GUI1

GUI1.main()
sopa = GUI1.sopa
coordenadas_dict = {}
words = GUI1.palabraBuscar

for x in words:
    coordenadas = ()
    coordenadas = algoritmo.buscapalabras(x, sopa)
    coordenadas_dict[x]= coordenadas
    
GUI2.main(coordenadas_dict, sopa)