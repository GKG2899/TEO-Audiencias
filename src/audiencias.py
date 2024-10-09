from collections import namedtuple
from csv import reader
SEPARADOR = ","
Audiencia = namedtuple("audiencia", "edicion, audiencia")
def lee_audiencias(nombre_fichero:str)->list[tuple[int,float]]:
    result = []
    with open(nombre_fichero, encoding="utf-8" ) as f:
        lector = reader(nombre_fichero)
        for lista_trozos in lector:
            #1,0.37
            
            edicion = str(lista_trozos[0])
            audiencia = float(lista_trozos[1])
            result.append(Audiencia(edicion, audiencia))
    return result
