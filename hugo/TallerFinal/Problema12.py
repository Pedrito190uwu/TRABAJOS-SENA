import random
import math

def generar_problema_88_12():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        # Mantener el triple como en el ejemplo original
        multiplicador = 3
        
        # Generar números aleatorios para el resto
        numero_base = random.randint(30, 100)  # Reemplaza al 55
        numero_comparacion = random.randint(150, 300)  # Reemplaza al 233
        
        # La ecuación es: 3x - numero_base = numero_comparacion - x
        # 3x + x = numero_comparacion + numero_base
        # 4x = numero_comparacion + numero_base
        # x = (numero_comparacion + numero_base) / 4
        
        numerador = numero_comparacion + numero_base
        
        if numerador % 4 == 0:
            x = numerador // 4
            
            # Verificar que los excesos sean positivos
            if 3*x > numero_base and numero_comparacion > x:
                print("\n" + "=" * 80)
                print("Ejercicio 88-12")
                print("=" * 80)
                print("Enunciado:")
                print(f"El exceso del triple de un número sobre {numero_base} equivale")
                print(f"al exceso de {numero_comparacion} sobre el número. Hallar el número.")
                print()
                print("Solución:")
                print(f"Sea x el número buscado")
                print(f"Exceso del triple sobre {numero_base}: 3x - {numero_base}")
                print(f"Exceso de {numero_comparacion} sobre x: {numero_comparacion} - x")
                print(f"Ecuación: 3x - {numero_base} = {numero_comparacion} - x")
                print(f"3x + x = {numero_comparacion} + {numero_base}")
                print(f"4x = {numerador}")
                print(f"x = {x}")
                print()
                print(f"Resultado: El número es {x}")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido.")

generar_problema_88_12()