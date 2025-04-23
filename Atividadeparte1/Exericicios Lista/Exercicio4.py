#tupla e contar quantos 4 tem

tupla1 = (1,2,2,3,4,4,4,4,4,5)
#provavelmente tem que converter para lista

lista = list (tupla1)
contador = lista.count(4)
tupla1 = list (tupla1)

print ("Quantidade de 4 presentes na tupla: {}, sendo a tupla {}".format (contador, tupla1))