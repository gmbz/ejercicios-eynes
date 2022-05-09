import random

filas = 5
columnas = 5


def genera_matriz():
    matriz = []
    for n in range(filas):
        fila = []
        for m in range(columnas):
            fila.append(random.randint(1, 10))
        matriz.append(fila)
    return matriz


def busca_secuencia_horizontal(matriz):
    for n in range(len(matriz)):
        secuencia = []
        size = len(matriz[0])
        m = 0
        while m < size:
            if m == size-1:
                if matriz[n][m-1]+1 == matriz[n][m]:
                    secuencia.append(matriz[n][m])
            elif matriz[n][m] == matriz[n][m+1]-1:
                if not secuencia:
                    posicion_inicial = (n, m)
                secuencia.append(matriz[n][m])
            if len(secuencia) == 4:
                posicion_final = (n, m)
                return secuencia, posicion_inicial, posicion_final
            m += 1
    return None, None, None


def busca_secuencia_vertical(matriz):
    for m in range(len(matriz[0])):
        secuencia = []
        size = len(matriz)
        n = 0
        while n < size:
            if n == size-1:
                if matriz[n-1][m]+1 == matriz[n][m]:
                    secuencia.append(matriz[n][m])
            elif matriz[n][m] == matriz[n+1][m]-1:
                if not secuencia:
                    posicion_inicial = (n, m)
                secuencia.append(matriz[n][m])
            if len(secuencia) == 4:
                posicion_final = (n, m)
                return secuencia, posicion_inicial, posicion_final
            n += 1
    return None, None, None


matriz = genera_matriz()

secuencia_horizontal, posicion_inicial_horizontal, posicion_final_horizontal = busca_secuencia_horizontal(
    matriz)
secuencia_vertical, posicion_inicial_vertical, posicion_final_vertical = busca_secuencia_vertical(
    matriz)

print(f"Matriz: {matriz}")

if secuencia_horizontal:
    print(f"Se encontró la secuencia horizontal: {secuencia_horizontal}")
    print(f"Posicion inicial: {posicion_inicial_horizontal}")
    print(f"Posicion final: {posicion_final_horizontal}")
else:
    print(f"No se encontró secuencia horizontal")
if secuencia_vertical:
    print(f"Se encontró la secuencia vertical: {secuencia_vertical}")
    print(f"Posicion inicial: {posicion_inicial_vertical}")
    print(f"Posicion final: {posicion_final_vertical}")
else:
    print(f"No se encontró secuencia vertical")

matriz = [
    [0, 5, 0, 4, 5],
    [0, 6, 7, 8, 9],
    [0, 7, 7, 6, 8],
    [0, 7, 6, 5, 10],
    [9, 8, 8, 1, 2]
]

secuencia_horizontal, posicion_inicial_horizontal, posicion_final_horizontal = busca_secuencia_horizontal(
    matriz)
secuencia_vertical, posicion_inicial_vertical, posicion_final_vertical = busca_secuencia_vertical(
    matriz)

print("------------------------------")
print(f"Matriz definida a mano: {matriz}")

if secuencia_horizontal:
    print(f"Se encontró la secuencia horizontal: {secuencia_horizontal}")
    print(f"Posicion inicial: {posicion_inicial_horizontal}")
    print(f"Posicion final: {posicion_final_horizontal}")
else:
    print(f"No se encontró secuencia horizontal")
if secuencia_vertical:
    print(f"Se encontró la secuencia vertical: {secuencia_vertical}")
    print(f"Posicion inicial: {posicion_inicial_vertical}")
    print(f"Posicion final: {posicion_final_vertical}")
else:
    print(f"No se encontró secuencia vertical")