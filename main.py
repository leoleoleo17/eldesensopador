import funciones
import GUI2
import prueba1


prueba1.main()
sopa = prueba1.sopa_
coordenadas_dict = {}
words = prueba1.palabraBuscar
print(words)
for x in words:
    coordenadas = ()
    coordenadas = funciones.buscapalabras(x, sopa)
    coordenadas_dict[x]= coordenadas
GUI2.main(coordenadas_dict, sopa)
