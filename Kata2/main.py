'''
Ejercicio 1

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribe un programa que comience leyendo el número de barras vendidas que no eson del día. Despues tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

'''


def ejercicio1():

    precio = 3.49
    descuento = 1 - 0.6 # El 100%, queremos descontar 40%, sería lo mismo que poner descuento = 0.4
    precioConDescuento = precio * descuento


    numero_de_barras = input("Introduce el número de barras vendidas: ")
    numero_de_barras = int(numero_de_barras)

    print("Precio habitual: " + str(precio) + "€")
    print ("Descuento: " + str(descuento))
    print("Coste final: " + str(numero_de_barras * precioConDescuento))


''' 
Escribir un programa que almacene la cadena de caracteres contaseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúscusñas y minúsculas.
'''

def ejercicio2():
    
    password = "contraseña"
    password_usuario = input("ingrese su contraseña: ")
    password_usuario = password_usuario.lower()

    if (password == password_usuario):
        print("El password es correcto")
    else:
        print("El password es incorrecto")
 

'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€, si es mayor a 18 años, 10€
'''

def ejercicio3():

    edad = int( input("Ingrese su edad:") )

    if (edad < 4):
        print("El precio de la entrada es 0")
    elif (edad >= 4 and edad <= 18):
        print("El precio de la entrada es 5€")
    else:
        print ("El precio de la entrada es 10€")

# Main

ejercicio3()
