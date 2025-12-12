"""
lista = ["Armenia", "Buenavista" ,  "Calarcá" , "Circasia" , "Córdoba" , "Genova" , "Filandia", "La tebaida" , "Montenegro" , "Pijao", "Quimbaya", "Salento" , ]

print(f"La lista completa es: {lista}")
print(f"Primer elemento de la lista: {lista[0]}")
print(f"Segundo elemento de la lista: {lista[1]}")
print(f"Tercer elemento de la lista: {lista[2]}")

lista[1] = "Buenavista"
lista[4] = "Córdoba"
print("Lista:", lista)
del(lista[0])
print("La Lista tiene un elemento menos:",len(lista))
del(lista[10])
print("Lista:", lista)
del lista # Borra la variable
#print("Lista:", lista)# descomentar esta línea de código y analizar el error
lista=["No hay"]
print(lista)

lista1 = ["a", "e" ,"i" ,"o" ,"u"]
print(lista1)
listaresultante = lista1 * 3
print(listaresultante)

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])
print(lista[2][6])



#Analizar
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lista)
lista1 = lista[1 : 5] # Imprime desde el primer indice hasta el (N-1) - 1
print(lista1)
lista2 = lista[: 5] # Imprime desde el indice 0 hatsa el N-1
print(lista2)
lista3 = lista[3 :] # Imprime desde el índice N hasta el final
print(lista3)

a = [1, 2, 3, 4]
a.append(5) # append agrega un elemento al final de la lista seleccionada
b = [6 , 7 , 8]
a.append(b)
c = "Hola"
a.append(c) #[1, 2, 3, 4, 5, [6, 7, 8], 'Hola’]
print(a)


a = [1, 2, 3, 4]
b = [6, 7, 8]
a.extend(b) # extend agrega los elementos de una lista ¡UNO POR UNO! al final de otra lista
c = "Hola"
a.extend(c)#[1, 2, 3, 4, 6, 7, 8, 'H', 'o', 'l', 'a’]
print(a)


lista = [45, 32, 3, 78]
print("Lista original: ", lista)
lista.append(995)
lista.append(7)
print("Lista después de usar append: ", lista)
lista.sort() # Ordena de menor a mayor
print("Lista ordenada: ", lista)
lista.reverse() # Pone la lista al revés
print("Lista al revés: ",lista)
listaextend = [1, 5, 87, 45]
lista.extend(listaextend)
print("Lista después de extend: ",lista)
lista.sort(reverse=True)
print("Lista ordenada al revés: ", lista)
print("Número de elementos 45: ",lista.count(45))
lista.insert(4, 111) # Inserta el elemento 111 en la posición 4
print("Lista después de insert: ",lista)
lista.remove(45) # Elimina la primera aparición del elemento 45
print("Lista después de remove: ", lista)
print("Posición del elemento 111: ",lista.index(111))
lista.pop() # Elimina el último elemento de la lista
print("Lista después de pop: ", lista)
lista.clear() # Elimina todos los elementos de la lista
print("Lista después de clear: ", lista)
"""








# Taller General
lista = ["Armenia", "Buenavista" ,  "Calarcá" , "Circasia" , "Córdoba"]
print("Lista inicial: ", lista)
print("Primer elemento:", lista[0])
print("Último elemento:", lista[-1])
lista.sort()
print("Lista ordenada:", lista)
# Listas vacias
lista_vacia = []
print("Lista vacía:", lista_vacia)
lista_vacia.append(23)
lista_vacia.append(True)
print("Lista vacía después del append:", lista_vacia)
listaextend = [1, 5, 87, 45]
listaextend.sort(reverse=True)
print("Lista ordenada:", listaextend)
lista.extend(listaextend)
print("Lista después de extend:", lista)
longitud = len(lista)
print("Longitud de la lista:", longitud)
del lista[2]
print("Lista después de eliminar el tercer elemento:", lista)
lista.remove("Circasia")
print("Lista después de eliminar 'Circasia':", lista)
elemento_eliminado = lista.pop()
print("Elemento eliminado con pop():", elemento_eliminado)
print("Lista después de pop():", lista)
listaDentroDeOtra = ["Quimbaya", "Salento"]
listaDentroDeOtra.append(listaextend)
print("Lista después de agregar otra lista con append():", listaDentroDeOtra)
print(listaDentroDeOtra[2][1])







"""
lista2 = lista.copy()
print("Lista original:", lista)
print("Copia de la lista:", lista2)

# Verificar si un elemento está en la lista
print("¿Está 'Calarcá' en la lista?", "Calarcá" in lista)
print("¿Está 'Genova' en la lista?", "Genova" in lista)

# Uso de range()
numeros = list(range(1, 11))  # Crea una lista de números del 1 al 10
print("Números del 1 al 10:", numeros)

for ciudad in range(len(lista)):
    print(lista[ciudad])

print(f"Lista después de agregar: {lista_vacia}")

numeros_pares = []
for i in range(0, 10, 2):
    numeros_pares.append(i)

print(f"Lista de pares: {numeros_pares}")

lista_mezclada = [
    "Hola Mundo",       # Cadena (str)
    45.5,               # Flotante (float)
    True,               # Booleano (bool)
    None,               # Tipo NoneType
    [1, 2, 3],          # Otra lista (list)
    {"clave": "valor"}  # Un diccionario (dict)
]

print(lista_mezclada)


# Conversion de cadenas a listas
saludo = "Python"

lista_caracteres = list(saludo)

print(lista_caracteres)
# Salida: ['P', 'y', 't', 'h', 'o', 'n']
"""
partes_iguales = "1/6"
print(partes_iguales[2])