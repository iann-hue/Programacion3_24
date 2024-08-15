#crear un programa que guarde en un diccionario las provincias argentinas
#con sus respectivas capitales, luego las muestre
provincias={"cordoba": cordoba, "jujuy": san salvador de jujuy, "salta": salta, "formosa": formosa, "tucuman": san miguel de tucuman, "chaco": residencia, "santiago del estero": ciudad de santiago del estero, "catamarca": san fernando del valle de catamarca, "corrientes": ciudad de corrientes, "misiones": tierra colorada, "santa fe": ciudad de santa fe, "la rioja": ciudad de la rioja, "entre rios": parana, "san juan": ciudad de san juan, "san luis": ciudad de san luis, "mendoza": mendoza, "buenos aires": la plata, "la pampa": ciudad de santa rosa, "neuquen": neuquen, "rio negro": viedma, "chubut": rawson, "santa cruz": rio gallegos, "tierra del fuego": ushuaia }

provinciabuscarvalorcapital=input ("Ingresar provincia a buscar capital: ")
#buscamos el valor por clave, en este caso capital ingresando provincia
x= provincias [provinciabuscarvalorcapital]
print ("su capital es: ", x)
print ("________________________")
#agregamos elemento al diccionario
provinciaagregar=input("ingrese la provincia que desea agregar: ")
capitalagregar=input("ingrese la capital que desea agregar: ")
provincias[pc.lagregar]=capitalpcia

print ("________________________")

for p, c in provincias.items():
    print (p, "-", c)