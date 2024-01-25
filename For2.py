print("For 2")

CantidadNumero = int(input("cantidad de números a introducir: "))
PrimerNumero = int(input("Introduce el primer número: "))

for i in range(CantidadNumero - 1):
    NumeroActual = int(input(f"Introduce el número {i + 2}: "))   

    if NumeroActual <= PrimerNumero:
        
         print(f"El número {NumeroActual} no es mayor que el primero ({PrimerNumero}).")
