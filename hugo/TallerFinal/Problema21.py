import random

def generar_problema_88_21():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        tienen = random.randint(10, 100)
        perdieran = random.randint(10, 100)
        
        denominador = 3 + 1
        numerador = 3*perdieran + tienen
        
        if numerador % denominador == 0:
            x = numerador // denominador
            
            print("Ejercicio 88-21")
            print("=" * 80)
            print("Enunciado:")
            print(f"Entre A y B tienen ${tienen}. Si A perdiera ${perdieran}, ")
            print(f"lo que tiene B sería el triple de lo que le quedaría a A. ¿Cuánto tiene cada uno?")
            print(f"Sea x lo que tiene A.")
            print(f"Como entre A y B tienen ${tienen}, entonces:")
            print(f"{tienen} - x es lo que tiene B")
            print(f"Si A perdiera ${perdieran}, entonces x - {perdieran} es lo que le quedaría a A")
            print(f"El problema indica “Si A perdiera ${perdieran}, lo que tiene B sería el triple de lo que le quedaría a A”, es decir:")
            print(f"{tienen} - x = 3(x - {perdieran})")
            print(f"{tienen} - x = 3x - {3*perdieran}")
            print(f"-x -3x = -{3*perdieran} -{tienen}")
            print(f"-4x = -{3*perdieran + tienen}")
            print(f"4x = {3*perdieran + tienen}")
            print(f"x = {3*perdieran + tienen} / 4")
            print(f"x = {x}")
            print()
            print(f"A tiene ${x}")
            print(f"B tiene ${tienen - x}")
            print(f"Entonces ${tienen - x} + ${x} = ${tienen}")
            
            print("\n" + "=" * 80)
            return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_21()