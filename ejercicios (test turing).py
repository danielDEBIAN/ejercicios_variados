from re import X

data = [1,2,3]
def incr(x):
    return x+1
print(data)

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3,[3,2,1])
f(3)

data=[10,20,30,40,50]
data.pop()
print(data)
data.pop(2)
print(data)

al = 'abcd'
for i in range(len(al)):
    al[i].upper()
print(al)

print(2**(3**2),(2**3)**2)

x = ['ab', 'cd']
print(list(map(lambda x: len(x),x)))