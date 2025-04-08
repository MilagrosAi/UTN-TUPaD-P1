"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla """

frase= input("Ingrese una frase o palabra por favor:")
longitudDeFrase = len(frase) -1

if frase[longitudDeFrase] == "a" or frase[longitudDeFrase] == "e" or frase[longitudDeFrase] == "i" or frase [longitudDeFrase] == "o" or frase[longitudDeFrase] =="u":
    print(f"{frase} !")
else: print(f"{frase}")
