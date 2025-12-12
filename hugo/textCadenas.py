# #a = "Hola"
# #b = 'Mundo'
# #c = "De la programacion 'en' Python"

# #print(a, b, c)

# cadena1 = input("Introduzca la primera cadena: ")
# cadena2 = input('Introduzca la segunda cadena: ')
# cadena3 = input('Introduzca la tercera cadena: ')

# #cadenaConSaltos = "\t" + cadena1 + "\n\t" + cadena2 + '\n\t' + cadena3 # \t es un tabulador
# #print("-------------- Cadena con saltos y tabuladores -------------------")
# #print(cadenaConSaltos)

# #print("-------------- Cadena SIN saltos y tabuladores -------------------")
# #cadenaSinSaltos = " ".join([cadena1, cadena2, cadena3])

# #print(cadenaSinSaltos)

# # Uso de funciones de texto
# # print("Longitud de la cadena2 (len):", len(cadena2))
# # print("Cadena3 toda a mayúsculas (upper):",cadena3.upper())
# # print("Cadena3 toda a minúsculas (lower):",cadena3.lower())
# # print("Cadena2 cambia de mayúsculas a minúsculas y viceversa (swapcase):",cadena2.swapcase())
# # print("Cadena1 la primera a mayúsculas (capitalize):",cadena1.capitalize())
# # print("Cadena2 la primera de cada palabra a mayúsculas (title):", cadena2.title())
# # print("¿Cadena1 todo minúsculas? (islower):", cadena1.islower())
# # print("¿Cadena3 todas mayúsculas? (isupper):", cadena3.isupper())
# # print("¿Cadena2 todos caracteres imprimibles? (isprintable):", cadena2.isprintable())
# # print("¿Cadena3 todos caracteres alfanuméricos? (isalnum):", cadena3.isalnum())
# # print("¿Cadena1 todos caracteres alfabéticos? (isalpha):", cadena1.isalpha())
# # print("¿Cadena3 la primera de cada palabra en mayúsculas y el resto minúsculas? (istitle):",cadena3.istitle())
# # print("¿Cadena2 todos los caracteres son espacios en blanco? (isspace):",cadena2.isspace())
# # print("¿Cadena1 todos dígitos? (isdigit):", cadena1.isdigit())
# # print("¿Cadena2 todos los caracteres con representación numérica? (isnumeric):",cadena2.isnumeric())
# # print("¿Cadena3 todos los caracteres son números con representación decimal? (isdecimal):",cadena3.isdecimal())
# # print("Carácter más alto de la cadena1 (max):", max(cadena1))
# # print("Carácter más bajo de la cadena3 (min):", min(cadena3))

# resultStartWith = cadena1.startswith("IRoNmAn", 7)
# resultEndWith = cadena2.endswith(cadena1)
# resultReplace = cadena3.replace("Soy", "Python")
# resultSplit = cadena1.split()
# resultSplitlines = cadena2.splitlines()
# resultFind = cadena3.find("CaPiTaN")
# print("¿La cadena1 empieza con la cadena2? (startswith):", resultStartWith)
# print("¿La cadena2 termina con la cadena2? (endswith):", resultEndWith)
# print("¿La cadena3 se sustituye por la cadena2? (replace):", resultReplace)
# print("¿La cadena1 es dividida en partes? (split):", resultSplit)
# print("¿La cadena2 es dividida en partes? (splitlines):", resultSplitlines)
# print("¿La cadena1 contiene la cadena2? (find):", resultFind)

# cadena = input("Introduzca una cadena: ")
# ValorABuscar = input("Introduzca el valor a buscar: ")
# resultStartWith = cadena.startswith(ValorABuscar)
# resultEndWith = cadena.endswith(ValorABuscar)
# Count = cadena.count(ValorABuscar)
# print("¿La cadena empieza con el valor buscado? (startswith):", resultStartWith)
# print("¿La cadena termina con el valor buscado? (endswith):", resultEndWith)
# print("¿Cuantas vecess de la cadena hay el valor buscado? (count):", Count)

# cadena = input("Introduzca una cadena: ")
# buscar = input("Introduzca una cadena para buscar:")
# print("La cadena aparece en la posición (find):", cadena.find(buscar))
# print("La cadena aparece en la posición (rfind):", cadena.rfind(buscar))

# cadena = input("Introduzca una cadena: ")
# reemplazar = input("Introduzca una subcadena de la anterior para reemplazar: ")
# reemplazo = input("Introduzca la cadena por la que se reemplazará la anterior: ")
# print("Cadena original:", cadena)
# print("Cadena nueva (replace):", cadena.replace(reemplazar, reemplazo))

# cadena = input("Introduzca una cadena con varias palabras: ")
# print("Cadena dividida por espacios en blanco (split):",cadena.split())

# # Split con parametro
# print("Cadena dividida por caracter \'a' (split):",cadena.split('a'))

# # Obtener los primeros n caracteres de una cadena:
cadena = "Python es gratis!"
print(cadena[0:5]) 

# Obtener una subcadena de tantos caracteres que inicia desde 0 + N , a partir del N-1 carácter de la cadena:
print(cadena[2:3])

  # Obtener el último carácter de la cadena:
print(cadena[-1]) 
  # Obtener los últimos N caracteres de una cadena:
print(cadena[-7:])

  #Una subcadena que contenga todos los caracteres excepto los últimos 4 caracteres y el 1.er carácter:
print(cadena[3:-5])

  # Obtener carácter intermedios de una cadena (uno si, otro no):
print(cadena[::2]) 

  #Invertir la cadena:
print(cadena[::-1])

 #Analizar
print("Longitud de la cadena:", len(cadena))
cadenalstrip = cadena.lstrip()
print("Cadena (lstrip):",cadenalstrip,end=".")
print("\nLongitud de la cadena (lstrip):", len(cadenalstrip))
cadenarstrip = cadena.rstrip()
print("Cadena (rstrip):",cadenarstrip,end=".")
print("\nLongitud de la cadena (rstrip):", len(cadenarstrip))
cadenastrip = cadena.strip()
print("Cadena (strip):",cadenastrip,end=".")
print("\nLongitud de la cadena (strip):", len(cadenastrip))


num1 = 83
num2 = 9
print(f"El producto de {num1} y {num2} es {num1 * num2}.")# Concatena de una forma mas ordenada
autor = "Guido van Rossum"
print(f"Principal autor de Python es {autor.title()}.") # Concatena y coloca el primer carácter en mayúscula
numero = 0.123456789
print(f'Formatear el número con cuatro dígitos: {numero:.6f}')  # Otra forma de redondear pero el ultimo numero se salta a partir de 4 digitos
print(f'Imprimir el valor como un porcentaje: {numero:.4%}') # Imprime el porcentaje
print(f'Formato exponencial: {numero:e}') # Imprime el número con exponente
numero = 200
print(f'El {numero} con 6 dígitos relleno de ceros es: {numero:06}') # Rellena con ceros a la izquierda hasta quedar con la cantidad ingresada de digitos
print(f'El número es {numero:+}')
numero = -25
print(f'El número es {numero:+}')
print(f'{numero :^40}')# Muestra el numero :^40 → centrado en 40 espacios
print(f'{numero*5 :^40}')# Muestra el numero :^40 → centrado en 40 espacios
print(f'{numero*100 :^40}')# Muestra el numero :^40 → centrado en 40 espacios
print(f'{"Python derecho :<40"}')
print(f'Python izquierdo :<40')
print(f'Python centrado :^40')
a = 400000000000.23# Asigna un número grande con decimales
# Muestra el número con separadores de miles (coma)
s = (f'${a:,.2f}')# la coma (,) agrega separadores de miles
print(s)
