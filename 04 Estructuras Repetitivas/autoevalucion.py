#Integrantes: Airalde Milagros Abril, Alterio Micaela, Ambrosio Laura Fernanda, Bravo Molins Daiana Mariel, Bruzoni Angelina Soledad


# Conversión de Números
# ---------------------
# Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.



# Preguntamos si es la opción 2: Conversión de Decimal a Binario.
elif (opcion == '2'):                                           


    # Le pedimos al usuario que ingrese  el número Decimal.
    num= input("Ingrese el número en decimal: ")        
    
    #Se genera un ciclo hasta que el usuario coloque un numero decial (incluyendo tanto positivos como negativos).
    while not num.lstrip("+-").isdigit():                        
        num= input("Ingrese el número en decimal: ")


    # Convertimos la variable signo a cadena.
    signo= ""


    # Obtenemos el signo del número decimal.
    for digito in num:
        if(digito == '-' or digito == '+'):        
            signo = digito


    # Convertimos el numero sin signo a entero.
    num= int(num.lstrip("+-"))


    # Declaramos el dividendo e iteramos para dividirlo por 2.         
    dividendo=num


    while dividendo !=0:
        #Guardamos el resto y modificamos el dividendo para continuar con la division.
        resto=dividendo%2
        dividendo=dividendo//2
        #Sumamos los restos a la variable
        num_binario= num_binario + str(resto) S


    #Invertimos la cadena para obtener el numero binario en orden.
    binario_invertido = num_binario[::-1]


    #Si el signo es + se imprimira el valor binario con un 1 adicional a la
    # izquierda indicando que es positivo y si es - , lo mismo pero se agregara a la izquierda un 0.
    if signo == '-' :
        bitSigno = 1
        print(f"\nEl numero {num} en binario es {bitSigno}{binario_invertido}")  
        print("Cuando el Decimal ingresado es Negativo se agrega a la izquierda del número binario traducido, el Bit de Signo 1.")


    else:
        bitSigno = 0
        print(f"\nEl numero {num} en binario es {bitSigno}{binario_invertido}") 
        print("Cuando el decimal ingresado es Positivo se agrega a la izquierda del número binario traducido, el Bit de Signo 0.")

