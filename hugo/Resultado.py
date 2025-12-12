#Distancia = float(input("A qué distancia viajó?" ))
#Tiempo = float(input("En cuantas horas viajó?" ))
#NombreConductor = input("¿Cuál es su nombre?" )
#Vehículo = input("En qué viajó?")

#Resultado = Distancia / Tiempo

#print(NombreConductor, " viajó en ", Vehículo, " a una velocidad promedio de ", round(Resultado, 4))

# Realizar un programa en Python que tome la variable y la imprima
# según se observa, NO usar librerias externas
#mi_nombre = "pepito PEREZ        peLAez   "

# Paso todo a minúscula
#nombre_limpio = mi_nombre.lower()

# Se eliminan los espacios, dejando solo 1
#resultado = ' '.join(nombre_limpio.split())

# Se pasa a mayúscula inicial la cadena
#resultado=resultado.title()

# Se imprime con un punto al final
#print(resultado,end=".")

#cadena = input("Introduzca una cadena con varias palabras: ")
#print("Cadena dividida por espacios en blanco (split):",cadena.split())

# Split con parametro
#print("Cadena dividida por caracter \'a' (split):",cadena.split('o'))

#suma = 150
#excede = 500

#menor = (suma - excede) / 2

#mayor = menor + excede

#print(f"La suma de dos números es {suma} y el mayor excede al mayor {excede}. Hallar los números")
#print("El número menor es: ", menor)
#print(f"El numero mayor es: {mayor}")
#print("Solución:")
#print("Sea x el número menor")
#print(f"Entonces x + {excede} es el número mayor")
#print(f"La suma de los dos números es {suma}, es decir")
#print(f"x + (x + {excede}) = {suma}")
#print("Resolviendo la anterior ecuación, tenemos:")
#print(f"x + (x + {excede}) = {suma}")
#print(f"2x + {excede} = {suma}")
#print(f"2x = {suma} - {excede}")
#print(f"2x = {suma - excede}/2")
#print(f"x = {(suma - excede)/2}")


#print(menor, " + (", menor, " + ", excede, ") = ", suma)

"""
Resta = 32
NumeroBase = 540

menor2 = (Resta - NumeroBase) / -2

NumeroMayor = menor2 + menor2

print(f"La resta de dos números es {NumeroBase} y su diferencia {Resta}. Hallar los números.")
print("El número menor es: ", menor2)
print(f"El numero mayor es: {NumeroMayor}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {menor2} + {menor2} es el número mayor")
print(f"La Resta de los números es {Resta}, es decir")
print(f"{NumeroMayor} - x - x = {Resta}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"{NumeroMayor} - x - x = {Resta}")
print(f"-2x = {Resta} - {NumeroBase}")
print(f"-2x =  {Resta - NumeroBase}")
print(f"(-1)-2x = {Resta - NumeroBase}(-1)")
positivo = (Resta - NumeroBase)*-1
print(f"2x =  {positivo}")
print(f"x =  {positivo}/2")
print(f"x =  {positivo/2}")

Respuesta = 1154
Disminuye = 506

menor = (Respuesta + Disminuye) / 2
mayor = menor - Disminuye

print(f"La respuesta de dos números es {Respuesta} y disminuye {Disminuye}. Hallar los números.")
print("El número menor es: ", menor)
print(f"El numero mayor es: {mayor}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {menor} - {Disminuye} es el número mayor")
print(f"La Respuesta de los números es {Respuesta}, es decir")
print(f"{menor} + ({menor} - {Disminuye}) = {Respuesta}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"{menor}  + ({menor} - {Disminuye}) = {Respuesta}")
print(f"2A = {Respuesta} + {Disminuye}")
print(f"2A =  {Respuesta + Disminuye}")
print(f"A =  {(Respuesta + Disminuye)}/2")
print(f"A = {(Respuesta + Disminuye)/2}")

Operación = 106
Suma = 24

Resultado = (Operación - Suma) / 2
mayorcito = Resultado + Resultado

print(f"La respuesta de dos números es {Operación} y excede {Suma}. Hallar los números.")
print("El número menor es: ", Resultado)
print(f"El numero mayor es: {mayorcito}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {Resultado} + {Resultado} es el número mayor")
print(f"La Respuesta de los números es {Operación}, es decir")
print(f"x + x + {Suma} = {Operación}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"x + x + {Suma} = {Operación}")
print(f"2x + {Suma} = {Operación}")
print(f"2x = {Operación} - {Suma}")
print(f"2x = {Operación - Suma}")
print(f"x = {Operación - Suma}/2")
print(f"x = {(Operación - Suma)/2}")

Igual = 56
Base = 14
B = (Igual + Base) / 2
A = B - Base

Base2 = B + B

print(f"La respuesta de dos números es {Igual} y su numero base es {Base}. Hallar los números.")
print("El número menor es: ", Igual)
print(f"El numero mayor es: {Base2}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {B} + {B} es el número mayor")
print(f"La Respuesta de los números es {Igual}, es decir")
print(f"A + B = {Igual}")
print(f"A = B - {Base}")
print(f"B - {Base} + B = {Igual}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"B - {Base} + B = {Igual}")
print(f"2B = {Igual} + {Base}")
print(f"2B = {Igual + Base}")
print(f"B = {Igual + Base}/2")
print(f"B = {(Igual + Base)/2}")


Objetivo = 1080
Basesita = 1014
Menorcito = (Objetivo - Basesita) / 2
May = Menorcito + Menorcito

print(f"La respuesta de dos números es {Objetivo} y su numero base es {Basesita}. Hallar los números.")
print("El número menor es: ", Objetivo)
print(f"El numero mayor es: {Basesita}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {Menorcito} + {Menorcito} es el número mayor")
print(f"La Respuesta de los números es {Igual}, es decir")
print(f"A + B = {Igual}")
print(f"A = B - {Base}")
print(f"B - {Base} + B = {Igual}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"B - {Base} + B = {Igual}")
print(f"2B = {Igual} + {Base}")
print(f"2B = {Igual + Base}")
print(f"B = {Igual + Base}/2")
print(f"B = {(Igual + Base)/2}")


menor = 67
intermedio = menor + 1
mayor = menor + 2
Resultado = 204

print(f"La respuesta de la operacion es {Resultado} y su ecuacion es {menor}. Hallar los números.")
print("El número menor es: ", menor)
print(f"El numero intermedio es: {intermedio}")
print(f"El numero mayor es: {mayor}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {menor} + 1 es el número intermedio")
print(f"Entonces {menor} + 2 es el número mayor")
print(f"La Respuesta de la operacion es {Resultado}, es decir")
print(f"x + x + 1 + x + 2 = {Resultado}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"x + x + 1 + x + 2 = {Resultado}")
print(f"3x + 3 = {Resultado}")
print(f"3x = {Resultado} - 3")
print(f"3x = {Resultado - 3}")
print(f"x = {Resultado - 3}/3")
print(f"x = {(Resultado - 3)/3}")


Resultado = 74
menor = 17
consecutivo1 = menor + 1
consecutivo2 = menor + 2
mayor = menor + 3

print(f"La respuesta de la operacion es {Resultado} y su ecuacion es {menor}. Hallar los números.")
print("El número menor es: ", menor)
print(f"Número consecutivo al anterior es: {consecutivo1}")
print(f"Número consecutivo al anterior es: {consecutivo2}")
print(f"El numero mayor es: {mayor}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {menor} + 1 es el número consecutivo al anterior")
print(f"Entonces {menor} + 2 es el número consecutivo al anterior")
print(f"Entonces {menor} + 3 es el número mayor")
print(f"La Respuesta de la operacion es {Resultado}, es decir")
print(f"x + x + 1 + x + 2 + x + 3 = {Resultado}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"x + x + 1 + x + 2 + x + 3 = {Resultado}")
print(f"4x + 6 = {Resultado}")
print(f"4x = {Resultado} - 6")
print(f"4x = {Resultado - 6}")
print(f"x = {Resultado - 6}/4")
print(f"x = {(Resultado - 6)/4}")


X = 48
Resultado = 194
PrimerPar = X * 2
print(f"La respuesta de la operacion es {Resultado} y su ecuacion es {X}. Hallar los números.")
print("El número menor es: ", X)
print(f"El numero mayor es: {PrimerPar}")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces {X} * 2 es el número mayor")
print(f"La Respuesta de la operacion es {Resultado}, es decir")
print(f"2x + 2x + 2 = {Resultado}")
print("Resolviendo la siguiente ecuación, tenemos:")
print(f"2x + 2x + 2 = {Resultado}")
print(f"4x + 2 = {Resultado}")
print(f"4x = {Resultado} - 2")
print(f"4x = {Resultado - 2}")
print(f"x = {Resultado -2}/4")
print(f"x = {(Resultado -2)/4}")

Caballo = 9000 + 8000
Arreros = 9000 - 2500
total = 32500
print(f"Se pagó un total de {total} pesos. Enotonces sus precios consecutivos son:")
print(f"El Caballo es de {Caballo} pesos")
print(f"El Arreros es de {Arreros} pesos")
print(f"Resolviendo la ecuación: ")
print(f"x + (x + 8000) + (x - 2500) = {total}")
print(f"x + x + 8000 + x - 2500 = {total}")
print(f"3x + 8000 - 2500 = {total}")
print(f"3x + 5500 = {total}")
print(f"3x = {total} - 5500")
print(f"3x = {total - 5500}")
print(f"x = {total - 5500}/3")
print(f"x = {(total - 5500)/3}")
print(f"El precio del coche es de {(total - 5500)/3} pesos")


Total = 200
print(f"La suma de tres números es 200. El mayor excede al del medio en 32 y al menor en 65. Hallar los números.")
print("El número menor es: ", Total)
print(f"El numero del medio es x - 32")
print(f"El numero menor es x - 65")
print("Solución:")
print("Sea x el número mayor")
print(f"x + (x - 32) + (x - 65) = {Total}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"x + (x - 32) + (x - 65) = {Total}")
print(f"x + x - 32 + x - 65 = {Total}")
print(f"3x - 97 = {Total}")
print(f"3x = {Total} + 97")
print(f"3x = {Total + 97}")
print(f"x = {Total + 97}/3")
print(f"x = {(Total + 97)/3}")
print(f"El número mayor es {(Total + 97)/3}")


Resultado = 575
SegundoCesto = Resultado - 10
TerceroCesto = Resultado - 15    

print(f"Tres cestos contienen {Resultado} manzanas. El primer cesto tiene 10 manzanas más que el segundo y 15 más que el tercero. ¿Cuántas manzanas hay en cada cesto?.")
print("El segundo cesto tiene: ", SegundoCesto)
print(f"El tercero cesto tiene: ", TerceroCesto)
print(f"Sea x el primer cesto")
print(f"Entonces x - 10 es el segundo cesto")
print(f"Entonces x - 15 es el tercero cesto")
print(f"x + (x - 10) + (x - 15) = {Resultado}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"x + (x - 10) + (x - 15) = {Resultado}")
print(f"x + x - 10 + x - 15 = {Resultado}")
print(f"3x - 25 = {Resultado}")
print(f"3x = {Resultado} + 25")
print(f"3x = {Resultado + 25}")
print(f"x = {Resultado + 25}/3")
print(f"x = {(Resultado + 25) / 3}")
print(f"El primer cesto tiene {(Resultado + 25) / 3} manzanas")


Resultado = 454
print(f"Dividir {Resultado} en tres partes sabiendo que la menor es 15 unidades menor que la del medio y 70 unidades menor que la mayor.")
print(f"El número menor es: x")
print(f"El número del medio es x + 15")
print(f"El número mayor es x + 70")
print("Solución:")
print("Sea x el número menor")
print(f"Entonces x + 15 es el número del medio")
print(f"Entonces x + 70 es el número mayor")
print(f"x + (x + 15) + (x + 70) = {Resultado}")
print("Resolviendo la anterior ecuación, tenemos:")
print(f"x + (x + 15) + (x + 70) = {Resultado}")
print(f"x + x + 15 + x + 70 = {Resultado}")
print(f"3x + 85 = {Resultado}")
print(f"3x = {Resultado} - 85")
Resta = Resultado - 85
print(f"3x = {Resta}")
print(f"x = {Resta}/3")
División = Resta / 3
print(f"x = {División} es la parte menor")


Resultado = 3100000
print(f"Repartir {Resultado} sucres entre tres personas de modo que la segunda reciba 200,000 menos que la primera y 400,000 más que la tercera.")
print(f"La primera persona recibe x + 200000")
print(f"La segunda persona recibe x")
print(f"La tercera persona recibe x - 400000")
print("Solución:")
print("Sea x la segunda persona")
print(f"(x + 200000) + x + (x - 400000) = {Resultado}")
print(f"x + 200000 + x + x - 400000 = {Resultado}")
print(f"3x - 200000 = {Resultado}")
print(f"3x = {Resultado} + 200000")
Suma = Resultado + 200000
print(f"3x = {Suma}")
print(f"x = {Suma}/3")
División = Suma / 3
print(f"x = {División}: la cantidad de la segunda persona")


Resultado = 88
print(f"La suma de las edades de tres personas es {Resultado} años. La mayor tiene 20 años más que la menor y la del medio 18 años menos que la mayor. Hallar las edades respectivas.")
print(f"La menor es x - 20")
print(f"La del medio es x - 18")
print(f"La mayor es x")
print("Solución:")
print("Sea x la mayor")
print(f"(x - 20) + (x - 18) + x = {Resultado}")
print(f"x - 20 + x - 18 + x = {Resultado}")
print(f"3 x - 38 = {Resultado}")
print(f"3 x = {Resultado} + 38")
print(f"3x = {Resultado + 38}")
print(f"x = {Resultado + 38} / 3")
print(f"x = {(Resultado + 38) / 3}")
print(f"La mayor tiene {(Resultado + 38) / 3} años")
print(f"La menor tiene {(Resultado + 38) / 3 - 20} años")
print(f"La del medio tiene {(Resultado + 38) / 3 - 18} años")
"""

print(f"Dividir 642 en dos partes tales que una exceda a la otra en 36.")
numero = 642
print(f"El numero base es x y su otro numero es x + 36")
print(f"Sea x el numero base")
print(f"Entonces x + 36 es el numero mayor")
print(f"x + (x + 36) = {numero}")
print(f"x + x + 36 = {numero}")
print(f"2x + 36 = {numero}")
print(f"2x = {numero} - 36")
print(f"2x = {numero - 36}")
print(f"x = {numero - 36}/2")
print(f"x = {(numero - 36)/2}")