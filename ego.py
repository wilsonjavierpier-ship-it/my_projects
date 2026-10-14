def sumar (a, b):
    return a + b 

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b 

def dividir (a, b):
    if  b != 0:
        return a/b

    else:
        return "Error: Division por cero"


    print("Menu de opciones:")
    print("Seleccione una operacion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")


opcion = input("Ingrese su opcion (1/2/3/4): ")
if opcion in ['1','2','3','4']:
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingresa el segundo numero: "))

        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"La suma es: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"La resta es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"La multiplicacion es: {resultado}")
        elif opcion == '4':
            resultado = dividir(num1, num2)
            print(f"La division es: {resultado}")
else:
    print("Opcion invalida")

