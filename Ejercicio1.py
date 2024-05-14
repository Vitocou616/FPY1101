
impares=0
pares=0

while True:
    try:

     numeros = int(input("Ingresa numeros al azar para que el programa vea cuales son pares e impares: "))

     if numeros == 0:
        break

     if numeros % 2 == 0:
        print("Este numero es par juju")
        pares += 1
    
     else:
        print("Este numero es impar.")
        impares += 1
    except ValueError:
        print("Error: Debe ingresar solo números para que el programa funcione correctamente.")

print("Total de pares:", pares)
print("Total de impares:", impares)