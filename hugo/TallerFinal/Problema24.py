import random

def generar_problema_88_24():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        # Generar números aleatorios
        total_pago = random.randint(50000, 500000)
        aumento = random.randint(5000, 50000)
        multiplicador = random.randint(2, 4)  # Puede ser doble, triple, etc.
        
        # La ecuación es: x + multiplicador*(x + aumento) = total_pago
        # Donde x es el precio del caballo más barato
        
        # x + m*x + m*aumento = total_pago
        # x*(1 + m) = total_pago - m*aumento
        # x = (total_pago - m*aumento) / (1 + m)
        
        numerador = total_pago - multiplicador * aumento
        
        if numerador % (1 + multiplicador) == 0 and numerador > 0:
            x = numerador // (1 + multiplicador)
            
            # Calcular precio del caballo caro
            precio_barato = x
            precio_caro = total_pago - x
            
            # Verificar que el caro sea mayor que el barato
            if precio_caro > precio_barato > 0:
                print("\n" + "=" * 80)
                print("Ejercicio 88-24")
                print("=" * 80)
                print("Enunciado:")
                print(f"Una persona compró dos caballos y pagó por ambos ${total_pago:,}.")
                print(f"Si el caballo de menor precio hubiera costado ${aumento:,} más,")
                print(f"el de mayor precio habría costado {multiplicador} veces ese nuevo precio.")
                print(f"¿Cuánto costó cada caballo?")
                print()
                
                print("Solución:")
                print(f"Sea x el precio del caballo más barato")
                print(f"El caballo caro cuesta: ${total_pago:,} - x")
                print()
                print(f"Si el barato costara ${aumento:,} más: x + ${aumento:,}")
                print(f"El caro costaría {multiplicador} veces eso: {multiplicador}(x + ${aumento:,})")
                print()
                print(f"Pero el caro realmente cuesta: ${total_pago:,} - x")
                print(f"Así que: {multiplicador}(x + ${aumento:,}) = ${total_pago:,} - x")
                print(f"{multiplicador}x + ${multiplicador*aumento:,} = ${total_pago:,} - x")
                print(f"{multiplicador}x + x = ${total_pago:,} - ${multiplicador*aumento:,}")
                print(f"({multiplicador + 1})x = ${total_pago - multiplicador*aumento:,}")
                print(f"x = ${total_pago - multiplicador*aumento:,} ÷ {multiplicador + 1}")
                print(f"x = ${precio_barato:,}")
                print()
                print(f"Precio caballo caro: ${total_pago:,} - ${precio_barato:,} = ${precio_caro:,}")
                print()
                print(f"Resultado:")
                print(f"Caballo barato: ${precio_barato:,}")
                print(f"Caballo caro: ${precio_caro:,}")
                print()
                print(f"Comprobación:")
                print(f"Si barato costara ${aumento:,} más: ${precio_barato + aumento:,}")
                print(f"El caro sería {multiplicador} veces eso: {multiplicador} × ${precio_barato + aumento:,} = ${multiplicador*(precio_barato + aumento):,}")
                print(f"Y realmente el caro cuesta: ${precio_caro:,} ✓")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")

generar_problema_88_24()