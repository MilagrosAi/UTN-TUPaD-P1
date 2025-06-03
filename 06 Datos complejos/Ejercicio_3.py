''') Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios. '''
precio_frutas = {"banana" :1200, "anana" : 2500 , "melon" : 3000, "uva" : 1450}

#Agrgo mas frutas
precio_frutas ["naraja"] = 1200
precio_frutas ["manzana"] = 1500
precio_frutas ["pera"] = 2300

print(precio_frutas)

#Actualizo los precios
precio_frutas["banana"] = 1330
precio_frutas["manzana"]= 1700
precio_frutas["melon"]= 2800

print(precio_frutas)

#Lista solo con los nombres
print(precio_frutas.keys())