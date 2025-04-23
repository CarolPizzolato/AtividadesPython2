#verificar se o numero é primo
''' preciso primeiro criar um loop para ver se o num pe divisivel por algo além dele e 1'''


num = []
for n in range(1,31):
    if n < 2:
        continue
    divisores  = 0
    for i in range (1,n+1): # isso é por causa do range que sempre tira -1
        if n % i == 0:
            divisores  += 1
    if divisores  == 2:
        num.append(n)
                    
print ("Os numeros primos são: ", num)
         
    
       