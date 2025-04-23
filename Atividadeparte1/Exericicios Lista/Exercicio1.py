#lista que armazena num digitados

list = []
for i in range(10):
    num = int(input("Digite um numero de 1 a 10: "))
    list.append(num) #cuidar o apend, não é java
    
    
#pode ser feito assim tambem com for, descobri como que é
for i in list:
    print (i)

#print (list) #não precisa de for