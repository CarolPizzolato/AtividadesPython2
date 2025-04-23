def verifica_valor (igual): #a função filter só pega um argumento
     x,y = igual
     return x == y
        
    
listaA  = [x for x in range(-10,5)]
listaB = [x for x in range(-10, 50)]

resultado = list(filter(verifica_valor, zip(listaA, listaB)))
print (resultado)

