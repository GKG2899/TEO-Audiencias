from audiencias import *
def main():
    listado_audiencias = lee_audiencias("data\GH_2.csv")
    tupla = listado_audiencias[0]
    print(listado_audiencias)
    print('Total de', len(listado_audiencias), " registros")

if __name__ == '__main__':
    main()
