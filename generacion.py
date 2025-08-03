import random
import secrets
from pprint import pprint

def revisar(lista : list[list[int]], copia : list[int]): 
    info = copia.copy()
    fila = []
    for i in range(9): 
        columna = [esto[i] for esto in lista]
        info = [dato for dato in info if not dato in columna and not dato in fila]
        random.shuffle(info)
        try: fila.append(info[0])
        except: fila.append(0)
        info = copia.copy()
    lista.append(fila)

def agregar(busqueda : list[list[dict]], cuadro : int, lista : list[int]): 
    if cuadro == 0: 
        for real, nuevo in zip(busqueda[cuadro], lista): 
            real['dato'] = nuevo
    else: 
        if cuadro == 3 or cuadro == 6: 
            real = [esto['dato'] for esto in busqueda[cuadro - 3]]
            real = [real[i:i + 3] for i in range(0, len(real), 3)]
            nuevo = []
            for i in range(3): 
                caso = []
                for esto in real: 
                    caso.append(esto[i])
                nuevo.append(caso)
            pprint(nuevo)
            inicio = nuevo.pop()
            nuevo.insert(0, inicio)
            pedazos = []
            for i in range(3): 
                caso = []
                for esto in nuevo: 
                    caso.append(esto[i])
                pedazos.append(caso)
            pprint(pedazos)
            lazos = []
            for esto in pedazos: lazos.extend(esto)
            for origen, real in zip(busqueda[cuadro], lazos): 
                origen['dato'] = real
        else: 
            real = [esto['dato'] for esto in busqueda[cuadro - 1]]
            real = [real[i:i + 3] for i in range(0, len(real), 3)]
            nuevo = real.copy()
            inicio = nuevo.pop()
            nuevo.insert(0, inicio)
            pedazos = []
            for esto in nuevo: pedazos.extend(esto)
            # pprint(nuevo)
            for origen, real in zip(busqueda[cuadro], pedazos): 
                origen['dato'] = real
    # i = 0
    # actuales = []
    # for n, cada in enumerate(busqueda[cuadro]): 
    #     i = n
    #     if cada['dato'] == 0: break
    #     else: actuales.append(cada['dato'])
    # info = busqueda[cuadro][i]
    # tabu = []
    # tabu.extend(actuales)
    # tabu.extend(obtener(busqueda, info['y'], 'y'))
    # tabu.extend(obtener(busqueda, info['x'], 'x'))
    # tabu = list(set(tabu))
    # pprint(tabu)
    # real = [esto for esto in lista if not tabu.__contains__(esto)]
    # try: busqueda[cuadro][i]['dato'] = random.choice(real)
    # except: pass

def obtener(busqueda : list[list[dict]], lugar : int, tipo : str): 
    todos = []
    for lista in busqueda: 
        for dato in lista: 
            if dato[tipo] == lugar and dato['dato'] != 0: 
                todos.append(dato['dato'])
    return todos

def crear(): 
    datos = list(range(1, 10))
    cuadritos = []
    filas = list(range(3))
    columnas = list(range(3))
    iniciof = 0
    finalf = 3
    inicioc = 0
    finalc = 3
    for _ in range(3): 
        filas = list(range(iniciof, finalf))
        columnas = list(range(inicioc, finalc))
        for _ in range(3): 
            lista = []
            for zona in filas: 
                for lado in columnas: 
                    lista.append({'dato': 0, 'y': zona, 'x': lado})
            cuadritos.append(lista)
            columnas = [cada + 3 for cada in columnas]
        iniciof += 3
        finalf += 3
        inicioc = 0
        finalc = 3
        # filas = [cada + 3 for cada in filas]
    version = cuadritos.copy()
    # cuadritos = [[{'dato': 0, 'x': j, 'y': i} for j in range(9)] for i in range(9)]
    cuadritos = version.copy()
    for i in range(9): 
        datos = datos.copy()
        random.shuffle(datos)
        agregar(cuadritos, i, datos)
        # for real, base in zip(datos, esto):
        #     base['dato'] = real
    return cuadritos

def vaciar(cuadritos : list[list[int]], quitadas : int): 
    datos = list(range(9))
    for _ in range(quitadas): 
        x = secrets.choice(datos)
        y = secrets.choice(datos)
        cuadritos[x][y] = 0
    return cuadritos

def reconstruir(cuadritos : list[list[dict]]): 
    matriz = [[0 for _ in range(9)] for _ in range(9)]
    for lista in cuadritos:
        for esto in lista: 
            matriz[esto['y']][esto['x']] = esto['dato']
    return matriz

def generar_matriz(): 
    matriz = []
    datos = list(range(1, 10))
    copia = datos.copy()
    random.shuffle(copia)
    # matriz.append(copia)
    # for _ in range(8): 
    #     copia = datos.copy()
    #     revisar(matriz, copia)
    #     pprint(matriz)
    for i in range(1, 10):
        copia = copia.copy()
        random.shuffle(copia)
        matriz.append(copia)
    real = crear()
    pprint(real)
    visual = reconstruir(real)
    pprint(real)
    final = vaciar(visual, 85)
    pprint(final)
    return final