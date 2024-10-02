from audiencias import lee_audiencias
def main():
    listado_audiencias = lee_audiencias('Proyectos de Teoría\TEO-Audiencias\data\GH.csv')
    print(listado_audiencias)
    print('Total de', len(listado_audiencias), " registros")

main()
#15:35 25-09-2024 funciona