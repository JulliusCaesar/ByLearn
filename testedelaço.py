def aumento_salario(salario): # Função para determinar o aumento de salário do Funcionário
    if salario <= 400: # 15% de aumento
        novo_salario = salario + (salario * 15 / 100) 
    elif salario <= 700: # 12% de aumento
        novo_salario = salario + (salario * 12 / 100)
    elif salario <= 1000: # 10% de aumento
        novo_salario = salario + (salario * 10 / 100)
    elif salario <= 1800: # 7% de aumento
        novo_salario = salario + (salario * 7 / 100)
    elif salario <= 2500: # 4% aumento
        novo_salario = salario + (salario * 4 / 100)
    elif salario > 2500: # 0% de aumento
        novo_salario = salario
    else:  # Não trabalha mais
        novo_salario = 0
        
    return novo_salario


def salario_media():
    # Média Salárial
    soma = 0
    for indice in somente_salario:
        soma += indice
    media_salarial = soma / len(somente_salario)

    return media_salarial

def fun_porcentagem():
    # Função que calcula a quantidade e porcentagem de funcionários que ganham acima da média salarial
    quantidade = 0
    for indice in somente_salario:
        if indice > media:
            quantidade += 1
    porcentagem = (quantidade / len(somente_salario)) * 100

    return print(f'O número de funcionário(s) que recebem acima da média salárial é: {quantidade} \nque corresponde a {porcentagem:.2f}% do total de funcionários')

colaborador = []
cadastro = []
somente_salario = []
somente_funcionario = []

# Entrada de dados
while True:
    # Laço de repetição para verificar duplicidade de cadastro
    while True:
        cadastro_funcionário = int(input('Digite o número do Funcionário: '))
# Criar IF para o número 0
        if cadastro_funcionário not in somente_funcionario:
            somente_funcionario.append(cadastro_funcionário)
            cadastro.append(cadastro_funcionário)
            break
        else:
            print('Valor duplicado!')
    cadastro.append(float(input('Digite o salário: ')))
    cadastro[1] = aumento_salario(cadastro[1])
    somente_salario.append(cadastro[1])
    
    print(f'O colaborador "{cadastro[0]}" receberá R$ {cadastro[1]:.2f}')
    
    del(cadastro[:])
    
    continuar = int(input('Deseja continuar? [0 = Não / 1 = Sim]: '))
    if continuar == 0: # Fim do Laço
        break

media = salario_media()
print('=' * 30)
print(f'O Maior Salário pago é: R$ {max(somente_salario):.2f}')
print(f'O Menor salário pago é: R$ {min(somente_salario):.2f}')
print(f'A média salárial da Empresa é: R$ {media:.2f}')
print(fun_porcentagem())