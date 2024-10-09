from sevici import *

def lee_sevici() -> None:
    lista_lineas = lee_estaciones("Proyectos de Teoría\\TEO-Audiencias\\data\\estaciones.csv")
    print(lista_lineas[1], 'es el primer registro')

def main():
    # Test de la función estaciones_bicis_libres
    libres1 = estaciones_bicis_libres(estaciones_sevici)
    print("Hay", len(libres1), "estaciones con 5 o más bicis libres:", libres1[:5])
    libres2 = estaciones_bicis_libres(estaciones_sevici, 10)
    print("Hay", len(libres2), "estaciones con 10 o más bicis libres:", libres2[:5])
    libres3 = estaciones_bicis_libres(estaciones_sevici, 1)
    print("Hay", len(libres3), "estaciones con al menos una bici libre:", libres3[:5])
