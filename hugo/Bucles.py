    
lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

for item in lista:
    print(item, end =" ")


listaabecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

listaiteraciones = [1,2,3,4,5]
for item in listaiteraciones:
    print("Iteración número: " + str(item))
    for letra in listaabecedario:
        print(letra, end = " ")
    print("\n----------------------------------------\n")

lista2=[2, 4, 6, 8, 10, 12]

for i in lista2:
    print( i * 10)
    if (i == 6):
        print("LLego al limite")
        break

nombre="La vida es bella"
for x in nombre:
    print(x.upper())

print("Inicio de programa:")

for i in [3, 4, 5]:
    print(f"Ahora i vale {i} y su cuadrado es: {i ** 2}")

print("Termino el programa")

texto = "Python"
for i in texto[::-1]:
    print(i)

contador = 1
for i in range(20 + 1):
    print("*" * i)
    contador += 1
    if contador == 10:
        break
print("Termina el programa")


multiplo = 7
contador = 0
for i in range(20):
    print(f"{multiplo} x {i} = {multiplo * i}")
    contador += 1
    if contador == 16:
        break
print("Termina tabla de multiplicar")


num = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"El factorial de {num} es: {factorial}")

edades = []

while True:
    cadena = input("Pulse enter para calcular, o escriba la edad de una persona: ")
    if cadena:
        edades.append(int(cadena))
    else:
        break


print("La edad mayor es: ", max(edades))
print("La menor edad es: ", min(edades))
print(f"El promedio de las {len(edades)} edades es: { round (sum (edades) / len (edades), 2 )}")


# TallerFinal.py
Contraseña = "Tomas69"
ingreso = input("Ingrese la contraseña para acceder al programa: ")
intentos = 3

while intentos >= 1:
    if ingreso == Contraseña:
        print(f"Acceso permitido")
        break
    else:
        intentos -= 1
        ingreso = input(f"Contraseña incorrecta. Le quedan {intentos} intentos. Intente de nuevo: ")
else:
    print("Acceso denegado. Ha agotado todos los intentos.")
    exit()

