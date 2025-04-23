
def divisao (a,b):
    
    try:
          return a/b
    except ZeroDivisionError:
       return  print ("ERRO: divisão por 0")    


def calculadora (num1,num2,operador):
    match operador:
        case '1':
            c = num1 + num2
            return  ("{} + {} = {}".format(num1,num2,c))
        case '2':
            c= num1 - num2
            return  ("{} - {} = {}".format(num1,num2,c))
        case '3': 
            c = num1 * num2
            return  ("{} * {} = {}".format(num1,num2,c))
        case '4':
            c = divisao (num1,num2)
            return  ("{} / {} = {}".format(num1,num2,c ))
        case _: return  ("Opção inavalida")
        
        
print ("========================Calculadora========================")

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input ("Digite a operação desejada \n1 [+] \n2 [-] \n3 [*] \n4 [/] \n")
    resultado = (calculadora (num1,num2,op))
    print (resultado)
    if resultado == "Opção inavalida":
        continue
    else:
        break
print ("========================FIM================================")