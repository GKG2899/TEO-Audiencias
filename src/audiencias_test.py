from audiencias import lee_audiencias
def main():
    listado_audiencias = lee_audiencias('H:\Other computers\My Computer\Universidad\Fundamentos de Programacion\Proyectos de Teoría\TEO-Audiencias\data\GH.csv')
    print(listado_audiencias)
    print('Total de', len(listado_audiencias), " registros")


main()
