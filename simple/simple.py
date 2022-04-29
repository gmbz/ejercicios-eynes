import random

def generar_listado():
    lista = []
    for i in range(1,11):
        edad = random.randint(1,100)
        elemento = {
            "id": i,
            "edad": edad
        }
        lista.append(elemento)
    return lista

def ordena_lista(lista):
    return sorted(lista, key=lambda elemento : elemento['edad'], reverse=True )

lista_ordenada = ordena_lista(generar_listado())

print(f"Lista: {lista_ordenada}")
print(f"ID de la persona mas vieja: {lista_ordenada[0]['id']}")
print(f"ID de la persona mas joven: {lista_ordenada[len(lista_ordenada)-1]['id']}")