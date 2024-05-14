suma = 0

numeropositivo = False

while not numeropositivo :
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n <= 0:
            print("Error: Debe ingresar un número entero positivo.")
        else:
            numeropositivo = True
    except ValueError:
        print("Error: Debe ingresar un número entero.")

for i in range(1, n + 1):
    suma += i

print("La suma de los primeros", n, "números es:", suma)