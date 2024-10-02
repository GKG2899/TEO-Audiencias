SEPARADOR = ","
def lee_audiencias(nombre_fichero:str)->list[tuple[int,float]]:
    result = []
    with open("Mi_FP_2425\fp_24_25\data\GH.csv") as f:
        for linea in f:
            #1,0.37
            lista_trozos = linea.split(SEPARADOR)
            edicion = int(lista_trozos[0])
            lee_audiencias = float(lista_trozos[1])
            result.append(edicion,linea)
    return result