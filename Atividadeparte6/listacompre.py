#revisar list  comprehension

#primeiro o básico
lista1 = [x for x in range(1,30)]
print (lista1)

#agora vamos selecionar somente multiplos de 3

lista2 = [x for x in range(1,30) if x % 3 == 0]
print (lista2)
