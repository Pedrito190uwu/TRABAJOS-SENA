import random

def generar_problema_88_27():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        # Generar números aleatorios
        multiplicador = random.randint(2, 5)
        caballos_mas = random.randint(1, 10)
        vacas_mas = random.randint(1, 10)
        multiplicador2 = random.randint(2, 3)
        
        if multiplicador == multiplicador2:
            intentos += 1
            continue
        
        denominador = multiplicador - multiplicador2
        numerador = multiplicador2 * vacas_mas - caballos_mas
        
        if denominador != 0 and numerador % denominador == 0 and numerador > 0:
            x = numerador // denominador
            
            # Asegurar que x > 0
            if x > 0:
                vacas = x
                caballos = multiplicador * x
                
                # Verificar que después de comprar más, también sea válido
                nuevas_vacas = vacas + vacas_mas
                nuevos_caballos = caballos + caballos_mas
                
                if nuevos_caballos == multiplicador2 * nuevas_vacas:
                    print("\n" + "=" * 80)
                    print("Ejercicio 88-27")
                    print("=" * 80)
                    print("Enunciado:")
                    print(f"Compré {multiplicador} veces más caballos que vacas.")
                    print(f"Si hubiera comprado {caballos_mas} caballos más y {vacas_mas} vacas más,")
                    print(f"tendría {multiplicador2} veces más caballos que de vacas.")
                    print(f"¿Cuántos caballos y cuántas vacas compré?")
                    print()
                    
                    print("Solución:")
                    print(f"Sea x el número de vacas compradas")
                    print(f"Como compré {multiplicador} veces más caballos que vacas:")
                    print(f"Número de caballos: {multiplicador}x")
                    print()
                    
                    print(f"Si hubiera comprado {caballos_mas} caballos más:")
                    print(f"  Caballos: {multiplicador}x + {caballos_mas}")
                    print()
                    
                    print(f"Si hubiera comprado {vacas_mas} vacas más:")
                    print(f"  Vacas: x + {vacas_mas}")
                    print()
                    
                    print(f"Después tendría {multiplicador2} veces más caballos que vacas:")
                    print(f"  {multiplicador}x + {caballos_mas} = {multiplicador2}(x + {vacas_mas})")
                    print()
                    
                    print(f"Resolviendo la ecuación:")
                    print(f"{multiplicador}x + {caballos_mas} = {multiplicador2}x + {multiplicador2 * vacas_mas}")
                    print(f"{multiplicador}x - {multiplicador2}x = {multiplicador2 * vacas_mas} - {caballos_mas}")
                    print(f"({multiplicador - multiplicador2})x = {multiplicador2 * vacas_mas - caballos_mas}")
                    print(f"{denominador}x = {numerador}")
                    print(f"x = {numerador} ÷ {denominador}")
                    print(f"x = {vacas} (número de vacas)")
                    print()
                    
                    print(f"Caballos: {multiplicador} x {vacas} = {caballos}")
                    print()
                    
                    print(f"Resultado:")
                    print(f"Vacas compradas: {vacas}")
                    print(f"Caballos comprados: {caballos}")
                    print()
                    
                    print(f"Comprobación:")
                    print(f"Actual: {caballos} = {multiplicador} x {vacas}")
                    print(f"Si comprara {caballos_mas} caballos más: {caballos + caballos_mas}")
                    print(f"Si comprara {vacas_mas} vacas más: {vacas + vacas_mas}")
                    print(f"Relación: {caballos + caballos_mas} = {multiplicador2} x {vacas + vacas_mas}")
                    return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_27()