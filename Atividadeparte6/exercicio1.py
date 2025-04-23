
def potencia (i): #nao esquece da var
    return 2**i

lista = [x for x in range (1,30)]

for i in map (potencia, lista):
    print (i)