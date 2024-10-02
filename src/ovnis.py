def lee_ovnis(nombre_fichero:str)->list[str]:
    result = []
    with open(nombre_fichero) as f:
        next(f)
        for linea in f 