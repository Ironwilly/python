#Escribe un programa que pida un nombre de usuario 
#y una contraseña y si se ha introducido “pepe” y “asdasd” 
#se indica “Has entrado al sistema”, sino se da un error.


usuario = input("Diga el nombre de usuario: ")
clave = input("Diga la contraseña: ")

if(usuario == 'pepe' and clave == 'asdasd'):
    print("Has entrado al sistema")

else:
    print("Error ")