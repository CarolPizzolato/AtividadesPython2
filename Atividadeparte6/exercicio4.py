def potencia2 (x):
    return x **2

def potencia3 (x):
    return x **3

lista = [0,1,2,3,4,5,6,7,8,9]

potencia2Lista = list(map(potencia2, lista))
print (potencia2Lista)

potencia3Lista = list(map(potencia3, lista))
print (potencia3Lista)
