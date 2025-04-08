hemiferio= input("En cual hemiferio se encuentra N/S?:")
mes= input("En que mes se encuentra?:")
dia= int(input("En que dia se encuentra?:"))

if hemiferio == "n":
    if((dia >= 21 and dia <= 31) and mes == "diciembre") or ((dia >= 1 and dia <=30) and mes == "enero") or ((dia >= 1 and dia <= 28) and mes == "febrero") or ((dia >= 1 and dia <=21) and mes == "marzo"): 
        print("estas en INVIERNO")
    elif ((dia >= 21 and dia <= 31) and mes == "marzo") or ((dia >= 1 and dia <=30) and mes == "abril") or ((dia >= 1 and dia <= 31) and mes == "mayo") or ((dia >= 1 and dia <=21) and mes == "junio"):
        print("estas en PRIMAVERA")
    elif ((dia >= 21 and dia <= 30) and mes == "junio") or ((dia >= 1 and dia <=31) and mes == "julio") or ((dia >= 1 and dia <= 31) and mes == "agosto") or ((dia >= 1 and dia <=21) and mes == "septiembre"):
        print("estas en VERANO")
    elif ((dia >= 21 and dia <= 30) and mes == "septimbre") or ((dia >= 1 and dia <=31) and mes == "octumbre") or ((dia >= 1 and dia <= 31) and mes == "noviembre") or ((dia >= 1 and dia <=20) and mes == "diciembre"):
        print("estas en OTOÑO")
elif hemiferio == "s":
    if ((dia >= 21 and dia <= 31) and mes == "diciembre") or ((dia >= 1 and dia <=30) and mes == "enero") or ((dia >= 1 and dia <= 28) and mes == "febrero") or ((dia >= 1 and dia <=20) and mes == "abril"):
        print("estas en VERANO")
    elif ((dia >= 21 and dia <= 31) and mes == "marzo") or ((dia >= 1 and dia <=30) and mes == "abril") or ((dia >= 1 and dia <= 31) and mes == "mayo") or ((dia >= 1 and dia <=20) and mes == "junio"):
        print("estas en OTOÑO")
    elif ((dia >= 21 and dia <= 31) and mes == "junio") or ((dia >= 1 and dia <=31) and mes == "julio") or ((dia >= 1 and dia <= 31) and mes == "agosto") or ((dia >= 1 and dia <=20) and mes == "septiembre"):
        print("estas en INVIERNO")
    elif ((dia >= 21 and dia <= 31) and mes == "septiembre") or ((dia >= 1 and dia <=31) and mes == "octubre") or ((dia >= 1 and dia <= 31) and mes == "noviembre") or ((dia >= 1 and dia <=20) and mes == "diciembre"):
        print("estas en Primavera")

