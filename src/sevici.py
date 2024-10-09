from csv import reader

SEPARADOR = ","
def lee_estaciones(nombre_fichero:str)->list[tuple[str,int,int,int,float,float]]:
    result = []
    
    with open("Mi_FP_2425\\fp_24_25\\data\\GH.csv") as f:
        lector = reader
        next(lector)
        for lista_trozos in lector:
           
            lista_trozos = linea.split(SEPARADOR)
            nombre = lista_trozos[0]
            numero_slots = int(lista_trozos[1])
            numero_slots_vacíos = int(lista_trozos[2])
            numero_bicis = int(lista_trozos[3])
            longitud = float(lista_trozos[4])
            latitud = float(lista_trozos[5])
            result.append(nombre,numero_slots,numero_slots_vacíos, numero_bicis,latitud,longitud)
    return result

def estaciones_bicis_libres(estaciones, k=5):
    ''' Estaciones que tienen bicicletas libres
    
    ENTRADA: 
      @param estaciones: lista de estaciones disponibles 
      @type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      @param k: número mínimo requerido de bicicletas
      @type k: int
    SALIDA: 
      @return: lista de estaciones seleccionadas
      @rtype: [(int, str)] 
    
    Toma como entrada una lista de estaciones y un número k.
    Crea una lista formada por tuplas (número de bicicletas libres, nombre)
    de las estaciones que tienen al menos k bicicletas libres. La lista
    estará ordenada por el número de bicicletas libres.
    '''
    pass

