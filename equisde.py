print("Hola amigos como estan")
i = 0
for i in range(5):
    print("*", sep=" ")
'''
Esto es un codigo de python que realiza la suma de dos numeros a partir de una definicion de una funcion
'''

def suma(a,b):
    return a+b

a = int(input("Dame el primer numero a sumar: "))
b = int(input("Dame el segundo numero a sumar: "))

print("La suma de los numeros es: ",suma(a,b))