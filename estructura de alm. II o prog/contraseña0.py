intentos=0
usuario_correcto= "usuario"
contraseña_correcto= "contraseña"
while intentos<3:
usuario=input ("ingrese el usuario: ")
contraseña=input ("ingrese la contraseña: ")
if usuario== usuario_correcto and contraseña== contraseña_correcto:
    print ("bienvenido al sistema")
    break #rompe el bucle si las credenciales estan correctas
intentos+=1
if intentos<3:
    print ("credenciales incorrectas, vuelve a intentarlo: ")
if intentos== 3:
    print ("ha intentado varias veces y ya llego al limite, adios")