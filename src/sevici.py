SEPARADOR = ","
def lee_estaciones(nombre_fichero:str)->list[tuple[str,int,int,int,float,float]]:
    result = []
    with open("Mi_FP_2425\\fp_24_25\\data\\GH.csv") as f:
        for linea in f:
           
            lista_trozos = linea.split(SEPARADOR)
            nombre = lista_trozos[0]
            numero_slots = int(lista_trozos[1])
            numero_slots_vacíos = int(lista_trozos[2])
            numero_bicis = int(lista_trozos[3])
            longitud = float(lista_trozos[4])
            latitud = float(lista_trozos[5])
            result.append(nombre,numero_slots,numero_slots_vacíos, numero_bicis,latitud,longitud)
    return result
