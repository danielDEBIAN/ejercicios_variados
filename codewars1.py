def array_diff(a, b):
    #your code here]
    tam = len(a)-1
    while tam>=0:
        if a[tam] in b:
            a.remove(a[tam])
        tam=tam-1
    return a

a = [1,2,2]
b = [2]
array = array_diff(a,b)
print(array)