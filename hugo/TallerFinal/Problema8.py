import random
import math

def generar_problema_88_8():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        # Generar años atrás/delante aleatorios
        años_pasado = random.randint(5, 20)
        años_futuro = random.randint(5, 20)
        
        # Generar múltiplos aleatorios
        multiplo_pasado = random.randint(2, 4)  # En el pasado
        multiplo_futuro = random.randint(2, 5)  # En el futuro
        menos_futuro = random.randint(10, 100)  # Lo que será menos
        
        # La ecuación es compleja, mejor generamos edades que cumplan
        # Probamos diferentes valores de x (edad de B)
        for x in range(20, 100):
            # Edad de A en el pasado
            A_pasado = multiplo_pasado * (x - años_pasado)
            # Edad actual de A
            A_actual = A_pasado + años_pasado
            # Edad de A en el futuro
            A_futuro = A_actual + años_futuro
            # Edad de B en el futuro
            B_futuro = x + años_futuro
            
            # Debe cumplir: A_futuro = multiplo_futuro * B_futuro - menos_futuro
            if A_futuro == multiplo_futuro * B_futuro - menos_futuro and A_actual > años_pasado:
                print("\n" + "=" * 80)
                print("Autor: Samuel Lara Grandas")
                print("Diciembre de 2025")
                print("Ejercicio 88-8 (Adaptación)")
                print("=" * 80)
                print("Enunciado:")
                print(f"Hace {años_pasado} años la edad de A era {multiplo_pasado} veces la de B y ")
                print(f"dentro de {años_futuro} años, la edad de A será {menos_futuro} años menos que ")
                print(f"{multiplo_futuro} veces la de B. Hallar las edades actuales.")
                print()
                print("Solución paso a paso:")
                print(f"Sea x la edad actual de B")
                print(f"Hace {años_pasado} años, B tenía x - {años_pasado}")
                print(f"A tenía {multiplo_pasado} veces eso: {multiplo_pasado}(x - {años_pasado})")
                print(f"Entonces la edad actual de A es: {multiplo_pasado}(x - {años_pasado}) + {años_pasado}")
                print()
                print(f"Dentro de {años_futuro} años:")
                print(f"B tendrá: x + {años_futuro}")
                print(f"A tendrá: [{multiplo_pasado}(x - {años_pasado}) + {años_pasado}] + {años_futuro}")
                print()
                print(f"Según el problema:")
                print(f"A_futuro = {multiplo_futuro}×B_futuro - {menos_futuro}")
                print(f"[{multiplo_pasado}(x - {años_pasado}) + {años_pasado}] + {años_futuro} = {multiplo_futuro}(x + {años_futuro}) - {menos_futuro}")
                print(f"{multiplo_pasado}x - {multiplo_pasado*años_pasado} + {años_pasado + años_futuro} = {multiplo_futuro}x + {multiplo_futuro*años_futuro} - {menos_futuro}")
                print(f"{multiplo_pasado}x - {multiplo_pasado*años_pasado - años_pasado - años_futuro} = {multiplo_futuro}x + {multiplo_futuro*años_futuro - menos_futuro}")
                print(f"{multiplo_pasado}x - {multiplo_futuro}x = {multiplo_futuro*años_futuro - menos_futuro + multiplo_pasado*años_pasado - años_pasado - años_futuro}")
                print(f"({multiplo_pasado - multiplo_futuro})x = {multiplo_futuro*años_futuro - menos_futuro + multiplo_pasado*años_pasado - años_pasado - años_futuro}")
                print(f"x = {(multiplo_futuro*años_futuro - menos_futuro + multiplo_pasado*años_pasado - años_pasado - años_futuro)/(multiplo_pasado - multiplo_futuro)}")
                print(f"x = {x} (edad de B)")
                print(f"Edad de A = {multiplo_pasado}({x} - {años_pasado}) + {años_pasado} = {A_actual}")
                print()
                print("Resultado final:")
                print(f"Edad actual de B: {x} años")
                print(f"Edad actual de A: {A_actual} años")
                print()
                print("Comprobación:")
                print(f"Hace {años_pasado} años: B tenía {x - años_pasado}, A tenía {A_actual - años_pasado}")
                print(f"  {A_actual - años_pasado} = {multiplo_pasado} × {x - años_pasado} ✓")
                print(f"Dentro de {años_futuro} años: B tendrá {x + años_futuro}, A tendrá {A_actual + años_futuro}")
                print(f"  {A_actual + años_futuro} = {multiplo_futuro} × {x + años_futuro} - {menos_futuro} ✓")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_8()