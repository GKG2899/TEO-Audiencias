from sevici import *

def lee_sevici() -> None:
    lista_lineas = lee_estaciones("Proyectos de Teoría\\TEO-Audiencias\\data\\estaciones.csv")
    print(lista_lineas[1], 'es el primer registro')

print(lee_sevici())