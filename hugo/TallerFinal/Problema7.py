import random
import math

def generar_problema_88_7():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        # Generar cantidad total aleatoria
        total = random.randint(50, 500)
        
        # Generar múltiplo aleatorio (2 a 6 veces)
        multiplo = random.randint(2, 6)
        
        # La ecuación es: total - x = multiplo * x
        # total = multiplo*x + x
        # total = x*(multiplo + 1)
        # x = total / (multiplo + 1)
        
        if total % (multiplo + 1) == 0:
            gasto = total // (multiplo + 1)
            queda = total - gasto
            
            print("\n" + "=" * 80)
            print("Autor: Samuel Lara Grandas")
            print("Diciembre de 2025")
            print("Ejercicio 88-7 (Adaptación)")
            print("=" * 80)
            print("Enunciado:")
            print(f"Tenía ${total}. Gasté cierta suma y lo que me queda es {multiplo} veces lo que gasté. ¿Cuánto gasté?")
            print()
            print("Solución paso a paso:")
            print(f"Sea x la cantidad gastada")
            print(f"Como tenía en total ${total}, entonces {total} - x es lo que queda sin gastar")
            print(f"Lo que queda es {multiplo} veces lo que gasté:")
            print(f"{total} - x = {multiplo}x")
            print(f"{total} = {multiplo}x + x")
            print(f"{total} = {multiplo + 1}x")
            print(f"x = {total} ÷ {multiplo + 1}")
            print(f"x = ${gasto}")
            print()
            print(f"Resultado: Se gastó ${gasto}")
            print(f"Comprobación: Lo que queda (${total-gasto}) es {multiplo} × ${gasto} = ${multiplo*gasto} ✓")
            return
            
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")

generar_problema_88_7()