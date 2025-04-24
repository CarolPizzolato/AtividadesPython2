
#agora vamos usar for j e k para um dicionario onde temos o nome e nota
#quero adicionar eu mesma os itens, entao vou tentar o input

dicionario = {}
for i in range(1,6):
    
    nome = input ("Digite o nome do aluno {}: ".format(i))
    
    if nome.isalpha():
        break
    else:
        print("Por favor digite um numero")
        
    nota = int(input ("Digite a nota do aluno {}: ".format(i)))
    dicionario[nome] = int(nota)

dicionario_resultado = {i: ('Aprovado' if j > 6 else 'Reprovado') for (i, j) in dicionario.items()}
print (dicionario_resultado)