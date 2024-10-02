def lee_audiencias(nombre_fichero:str)->list[str]:
    result = []
    with open("Proyectos de Teoría\TEO-Audiencias\data\GH.csv") as f:
        for linea in f:
            result.append(linea)
    return result