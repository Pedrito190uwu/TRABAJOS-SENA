# p1=3
# p2=2
# p3=5
# p4=7

# x = ((p1/p2) + (p2/p3)) / ((p1/p2) - (p2/p3))
# print(x)

# x2 = p1 + ( (p1 + ((p1 + p2) / (p3 + p4))) / (p1 + (p1 / p2)))
# print(x2)

# x3 = (p1 + p2 + (p3 / (p4 * p1))) /  (p1 + p2 * (p3 / p4))
# print(x3)

# x4 = (p1 + p2 + p3) / (p1 + (p2 / p3))
# print(x4)

# x5 = ( (p1 + (p2 / ( p1 + p2 + (p2 / p3))))) / (p1 + (p2 / (p3 + p1)))
# print(x5)

# x6 = (p1 + (p2 / p3) - p4) / (p1 + (p2 / (p3**p4 + (p4 / (p1 - (p2 / p3) * p4)))))
# print(x6)

# x7 = p1 + (p2 / (p3 + p4))
# print(x7)

# x8 = ((p1 + p2) / p3) + p4
# print(x8)

# x9 = p1 + ( p2 / p3 ) + p4
# print(x9)

# x10 = (p1 + p2) / (p3 + p4)
# print(x10)

# print (p1,p2,p3,p4, sep=', ')
# print (p1,p2,p3,p4, end=', ')


# print("Primera línea: \"Texto entre comillas\"\nSegundo renglón: \'\x40\'")

p1 = float(input("Ingrese un número entero: "))
n2 = float(input("Ingrese otro número entero: "))
n3 = float(input("Ingrese otro número entero: "))
n4 = float(input("Ingrese otro número entero: "))
n5 = int(input("Ingrese otro número entero: "))
n6 = int(input("Ingrese otro número entero: "))

# suma = p1 + n2
# print("Suma: ", suma)
# resta = p1 - n2
# print("Resta: ", resta)
# multiplicación = p1 * n2
# print("multiplicación: ", multiplicación)
# cociente = p1 / n2
# print("Cociente: ", cociente)
# residuo = p1 % n2
# print("Residuo: ", residuo)
# potencia = p1 ** n2
# print("Potencia: ", potencia)
# division_entera = p1 // n2
# print("División entera: ", division_entera)

# numero = complex(float(input("Parte real: ")), float(input("Parte imaginaria:")))
# print(numero)

# resultado = (n5 + (n3 * (p1 ** n6))) - (n4 // n2)
# print("El resultado es: ", resultado)


#boolean1 = bool(input("Primer valor: "))
#boolean2 = bool(input("Segundo valor: "))
#boolean3 = bool(input("Tercer valor: "))
#boolean4 = bool(input("Cuarto valor: "))
#boolean5 = bool(input("Quinto valor: "))
#print("Resultado: ", boolean4 or ((boolean3 and not boolean2) and boolean1) or boolean5)
#print(not boolean2)

print(f'{p1} == {n4} : {p1 == n4}')
print(f'{n2} != {n3} : {n2 != n3}')
print(f'{n3} > {n2} : {n3 > n2}')
print(f'{n4} < {p1} : {n4 < p1}')
print(f'{p1} >= {n2} : {p1 >= n2}')
print(f'{n3} <= {n4} : {n3 <= n4}')

#p1 y n2
numero1 = float(input("Ingrese un número entero: "))
numero2 = float(input("Ingrese otro número entero: "))
print("Suma: ", numero1 + n2)
print("Resta: ", numero1 - n2)
print("Multiplicación: ", numero1 * n2)
print("Cociente: ", numero1 / n2)
print("Residuo: ", numero1 % n2)
print("Potencia: ", numero1 ** n2)
print("División entera: ", numero1 // n2)