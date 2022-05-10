import random

def generar_listado():
    """
    >>> lista = generar_listado()

    >>> len(lista) == 10
    True
    >>> lista[0]['id'] == 1
    True
    >>> lista[len(lista)-1]['id'] == 10
    True
    """
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
    """
    >>> lista = ordena_lista(generar_listado())
    
    >>> len(lista) == 10
    True
    >>> lista[0]['edad'] > lista[len(lista)-1]['edad']
    True
    """
    return sorted(lista, key=lambda elemento : elemento['edad'], reverse=True )

lista_ordenada = ordena_lista(generar_listado())
print(f"Lista: {lista_ordenada}")
print(f"ID de la persona mas vieja: {lista_ordenada[0]['id']}")
print(f"ID de la persona mas joven: {lista_ordenada[len(lista_ordenada)-1]['id']}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()