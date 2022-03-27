def isValid(s: str) -> bool:
    abiertos = 0
    for c in s:
        if c == '(':
            abiertos+=1
        elif c == '[':
            abiertos+=1
        elif c == '{':
            abiertos+=1
        if c == ')':
            abiertos-=1
        elif c == ']':
            abiertos-=1
        elif c == '}':
            abiertos-=1
        if abiertos<0:
            return False
    if abiertos==0:
        return True
    else:
        return False
        
line = input()
if isValid(line):
    print("Valid")
else:
    print("Invalid")