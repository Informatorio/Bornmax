def suma(a,b):
    return a+b

def multiplicacion(a,b):
    resul = a
    for i in range(1,b):
        resul = resul + a
    return resul

print(multiplicacion(3,3))
