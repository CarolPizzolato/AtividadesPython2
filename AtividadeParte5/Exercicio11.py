# o exercicio 1 eu ja sei fazer
#vou ir pro 2

lista = []

for i in range(6):
    adiciona = input ("Digite uma fruta para lista: ").strip()
    lista.append(adiciona)
    
minusculo = [i.lower() for i in lista]

#para garantir que sempre seja encontrado o morango podemos colocar um .upper or .lower
if "morango" in minusculo:
    print("Morango está na lista")
else:
    print("Morango não está na lista")