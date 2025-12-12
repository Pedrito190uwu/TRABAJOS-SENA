
# Online Python - IDE, Editor, Compiler, Interpreter


def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')


def saludar(nombre):
    print(f'Hola {nombre}')
    
saludar("Lara")


# Menu de opciones

def menu(num_1, num_2):
    opcion = input("¿Qué quieres hacer? \n1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Salir \n")
    if opcion == "1":
        resultado = num_1 + num_2
        return resultado
    elif opcion == "2":
        resultado = num_1 - num_2
        return resultado
    elif opcion == "3":
        resultado = num_1 * num_2
        return resultado
    elif opcion == "4":
        resultado = num_1 / num_2
        return resultado
    elif opcion == "5":
        print("Adiós!")
        exit()
    else:
        print("Opción no válida")

llamada = menu(5, 3)
print(llamada)


def menu_restaurante():
    opcion = input("¿Qué quires pedir? \n1. Pedir comida \n2. Pedir bebida \n3. Pedir las dos cosas \n4. Pedir postre \n 5. Pedir todo completo \n 6. Salir \n")
    
    if opcion == "1":
        print("Pedimos comida")
        opcionComida = input("¿Qué comida quieres? \n1. Pizza $20000 \n2. Hamburguesa $15000 \n3. Tacos $10000 \n4. Salsa $8000 \n5. Sopa $12000 \n6. Salir \n")
        if opcionComida == "1":
            print("Pedimos pizza")
            return "Pagar $20000"
        elif opcionComida == "2":
            print("Pedimos hamburguesa")
            return "Pagar $15000"
        elif opcionComida == "3":
            print("Pedimos tacos")
            return "Pagar $10000"
        elif opcionComida == "4":
            print("Pedimos salsa")
            return "Pagar $8000"
        elif opcionComida == "5":
            print("Pedimos sopa")
            return "Pagar $12000"
        elif opcionComida == "6":
            print("Adiós!")
            exit()
        else:
            print("Opción no válida")
    elif opcion == "2":
        print("Pedimos bebida")
        opcionBebida = input("¿Qué bebida quieres? \n1. Coca $100 \n2. Vino $50 \n3. Salsa $20 \n4. Sopa $10 \n5. Salir \n")
        if opcionBebida == "1":
            print("Pedimos coca")
            return "Pagar $100"
        elif opcionBebida == "2":
            print("Pedimos vino")
            return "Pagar $50"
        elif opcionBebida == "3":
            print("Pedimos salsa")
            return "Pagar $20"
        elif opcionBebida == "4":
            print("Pedimos sopa")
            return "Pagar $10"
        elif opcionBebida == "5":
            print("Adiós!")
            exit()
        else:
            print("Opción no válida")
    elif opcion == "3":
        print("Pedimos postre")
        opcionPostre = input("¿Qué postre quieres? \n1. Brownie $100 \n2. Tortilla $50 \n3. Helado $20 \n4. Chiscake $10 \n5. Salir \n")
        if opcionPostre == "1":
            print("Pedimos brownie")
            return "Pagar $100"
        elif opcionPostre == "2":
            print("Pedimos Tortilla")
            return "Pagar $50"
        elif opcionPostre == "3":
            print("Pedimos Helado")
            return "Pagar $20"
        elif opcionPostre == "4":
            print("Pedimos Chiscake")
            return "Pagar $10"
        elif opcionPostre == "5":
            print("Adiós!")
            exit()
        else:
            print("Opción no válida")
    elif opcion == "4":
        print("Pedimos comida y bebida")
        opcionComida = input("¿Qué comida quieres? \n1. Pizza $20000 \n2. Hamburguesa $15000 \n3. Tacos $10000 \n4. Salsa $8000 \n5. Sopa $12000 \n6. Salir \n")
        if opcionComida == "1":
            print("Pedimos pizza")
            return "Pagar $20000"
        elif opcionComida == "2":
            print("Pedimos hamburguesa")
            return "Pagar $15000"
        elif opcionComida == "3":
            print("Pedimos tacos")
            return "Pagar $10000"
        elif opcionComida == "4":
            print("Pedimos salsa")
            return "Pagar $8000"
        elif opcionComida == "5":
            print("Pedimos sopa")
            return "Pagar $12000"
        elif opcionComida == "6":
            print("Adiós!")
            exit()
        else:
            print("Opción no válida")
        opcionBebida = input("¿Qué bebida quieres? \n1. Coca $100 \n2. Vino $50 \n3. Salsa $20 \n4. Sopa $10 \n5. Salir \n")
        if opcionBebida == "1":
            print("Pedimos coca")
            return "Pagar $100"
        elif opcionBebida == "2":
            print("Pedimos vino")
            return "Pagar $50"
        elif opcionBebida == "3":
            print("Pedimos salsa")
            return "Pagar $20"
        elif opcionBebida == "4":
            print("Pedimos sopa")
            return "Pagar $10"
        elif opcionBebida == "5":
            print("Adiós!")
            exit()
        else:
            print("Opción no válida")
    else:
        print("Opción no válida") 
        
print(menu_restaurante())
