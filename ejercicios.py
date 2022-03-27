'''
Crear una funcion llamada removeDuplicates la cual 
dado un array no ordenado retorna un nuevo array 
sin elementos y a su vez ordenado
'''
def removeDuplicates(array):
    aux = []
    for n in range(len(array)):
        if array[n] not in aux:
            aux.append(array[n])
    aux.sort()
    return aux

array = [1,2,5,3,2,3,4,5,1,1,6,6,7]
array = removeDuplicates(array)
print("Array ordenado y sin duplicados: "+str(array))

'''
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
'''
def max(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2

num1=6
num2=21
mayor = max(num1,num2)
print("Numero mayor: "+str(mayor))

'''
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
'''
def max_from_three(n1,n2,n3):
    if n1==n2==n3:
        return n1

    if n1==n2 & n1>n3:
        return n1
    elif n3>n1:
        return n3

    if n1==n3 & n1>n2:
        return n1
    elif n2>n1:
        return n2
    
    if n2==n3 & n2>n1:
        return n2
    elif n1>n2:
        return n1

    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    if n2>n1:
        if n2>n3:
            return n2
        else:
            return n3
    if n3>n1:
        if n3>n2:
            return n3
        else:
            return n2
    
n1=12
n2=123
n3=1
mayor = max_from_three(n1,n2,n3)
print("Numero mayor: "+str(mayor))

'''
Definir una función que calcule la longitud de una lista o una cadena dada.
(No cuenta los espacios)
'''
def long_cad(s):
    aux=0
    for i in s:
        if i==" ":
            aux+=0
        else:
            aux+=1
    return aux

cadena = "Hola Amigos"
tam = long_cad(cadena)
print("Tamaño de la cadena: "+str(tam))

'''
Escribir una función que tome un carácter y devuelva True si es una vocal, 
de lo contrario devuelve False.
'''
def vocal(a):
    aux = ["a","e","i","o","u","A","E","I","O","U"]
    if a in aux:
        return True
    else:
        return False
car = "h"
if vocal(car):
    print("Es vocal")
else:
    print("No es vocal")

'''
Escribir una función sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista.
'''
def sum(array):
    aux=0
    for n in range(len(array)):
        aux+=array[n]
    return aux
def multip(array):
    aux=1
    for n in range(len(array)):
        aux *= array[n]
    return aux

array = [1,2,3,4]
suma = sum(array)
multipl = multip(array)
print("Suma del array: "+str(suma))
print("Multiplicacion del array: "+str(multipl))

'''
Definir una función inversa() que calcule la inversión de una cadena.
'''
def inversa(cadena):
    tam = -(len(cadena)-1)
    new = ""
    for n in range(tam,1):
        n = abs(n)
        new += cadena[n]
    return new

cadena = "Hola Amigos"
inv = inversa(cadena)
print("Cadena inversa: "+inv)

'''
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas)
'''
def es_palindromo(cadena):
    cadena = str(cadena).lower()
    cadena = cadena.replace(" ","")
    inver = inversa(cadena)
    if cadena==inver:
        return True
    else:
        return False

cadena = "Anita lava la tina"
if es_palindromo(cadena):
    print("Es palindromo")
else:
    print("No es palindromo")

'''
Definir una función superposicion() que tome dos listas y devuelva True 
si tienen al menos 1 miembro en común o devuelva False de lo contrario.
'''
def superposicion(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                return True
    return False
l1 = [1,2,3,4]
l2 = [5,6,7,8,3]
if superposicion(l1,l2):
    print("Las listas tienen elementos en comun")
else:
    print("Las listas no tienen elementos en comun")

'''
Definir una función generar_n_caracteres() que tome un entero n 
y devuelva el caracter multiplicado por n.
'''
def generar_n_carac(n,a):
    aux = ""
    for i in range(n):
        aux+=a
    return aux # Esta funcion tambien puede retornar solo n*a
num = 5
carac = "x"
rep = generar_n_carac(num,carac)
print("String generado: "+rep)

'''
Definir un histograma procedimiento() que tome una lista de 
números enteros e imprima un histograma en la pantalla.
'''
def procedimiento(array):
    for i in range(len(array)):
        print(str(array[i]*"*"))
array = [4,9,7]
procedimiento(array)