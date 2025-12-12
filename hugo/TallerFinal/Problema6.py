import random
import math

def generar_problema_88_6():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        # Generar largo aleatorio
        largo = random.randint(200, 1000)
        
        # Generar múltiplo aleatorio (3 a 12 veces el ancho)
        multiplo = random.randint(3, 12)
        
        # Generar exceso aleatorio
        exceso = random.randint(5, 50)
        
        # La ecuación es: largo = multiplo * ancho + exceso
        # ancho = (largo - exceso) / multiplo
        
        numerador = largo - exceso
        
        if numerador % multiplo == 0 and numerador > 0:
            ancho = numerador // multiplo
            
            print("\n" + "=" * 80)
            print("Autor: Samuel Lara Grandas")
            print("Diciembre de 2025")
            print("Ejercicio 88-6 (Adaptación)")
            print("=" * 80)
            print("Enunciado:")
            print(f"El largo de un buque es {largo} pies, y excede en {exceso} pies a {multiplo} veces el ancho. Hallar el ancho.")
            print()
            print("Solución paso a paso:")
            print(f"Sea x el ancho del buque")
            print(f"El largo ({largo} pies) excede en {exceso} pies a {multiplo} veces el ancho")
            print(f"Esto significa: {largo} = {multiplo}x + {exceso}")
            print(f"{multiplo}x = {largo} - {exceso}")
            print(f"{multiplo}x = {largo - exceso}")
            print(f"x = {largo - exceso} ÷ {multiplo}")
            print(f"x = {ancho}")
            print()
            print(f"Resultado: El ancho del buque es {ancho} pies")
            print(f"Comprobación: {multiplo} × {ancho} + {exceso} = {multiplo*ancho + exceso} = {largo} ✓")
            return
            
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")

generar_problema_88_6()