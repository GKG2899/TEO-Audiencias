from datetime import datetime
def lee_ovnis(nombre_fichero:str)->list[str]:
    result = []
    with open(nombre_fichero, encoding="utf-8") as f:
        next(f)
        for linea in f:
            trozos = linea.split(",")
            fecha = datetime.strftime(trozos[0], "%m/%d/%y %H:%M")
            ciudad = trozos.strip(1)
            estado = trozos.strip[2]
            forma = trozos.strip[3]
            duracion = trozos.strip[4]
            comentarios = trozos.strip[5]
            latitud = trozos.strip[6]
            longitud = trozos.strip[7]
            lista = (fecha, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            print(lista)
            