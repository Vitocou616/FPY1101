
texto = input("Ingrese una palabra para analizar cuantas vocales y consonantes tiene: ")

vocales = 0
consonantes = 0

for caracter in texto:
    if caracter.isalpha():
        if caracter in "aeiou":
            vocales += 1
        else:
            consonantes +=1
    else:
        print("La palabra contiene un caracter que no es una letra")

print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)