import random
import math

def generar_problema_88_18():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        # Generar números aleatorios
        dentro_de = random.randint(1, 10)
        años_despues = random.randint(1, 20)
        
        # Según la fórmula: x = años_despues - dentro_de
        # Para que x sea positivo: años_despues > dentro_de
        if años_despues > dentro_de:
            x = años_despues - dentro_de  # Edad de B
            A = 3 * (x + dentro_de) - dentro_de  # Edad de A
            
            print("\n" + "=" * 80)
            print("Ejercicio 88-18")
            print("=" * 80)
            print("Enunciado:")
            print(f"Dentro de {dentro_de} años la edad de A será el triple de la de B,")
            print(f"y {años_despues} años después la edad de A será el doble de la de B.")
            print(f"Hallar las edades actuales.")
            print()
            
            print("Solución:")
            print(f"Ecuación: 3(x + {dentro_de}) + {años_despues} = 2(x + {dentro_de} + {años_despues})")
            print(f"3x + {3*dentro_de} + {años_despues} = 2x + {2*(dentro_de + años_despues)}")
            print(f"x = {años_despues - dentro_de}")
            print()
            print(f"Edad de B: {x} años")
            print(f"Edad de A: {A} años")
            return
            
        intentos += 1
    print("No se pudo generar un problema válido.")

generar_problema_88_18()