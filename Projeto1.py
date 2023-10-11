#programa um sistema de cobrança de banho para um petshop - interface com o funcionário
#cobrança é feita a partir do peso do cachorro, do tamanho do pelo e de acréscimos de outros serviços

#início da função cachorro_peso
def cachorro_peso():
    while True:
        try:
            peso = float(input("Informe o peso do cachorro: "))
            if peso >= 50:
                print('Não aceitamos cachorros tão grandes.')
                print('Por favor, digite o peso novamente.')
                print('')
                continue #volta para o início da função para que o usuário digite um peso válido
            else:
                print('')
                if peso < 3:
                    return 40
                elif 3 < peso < 10:
                    return 50
                elif 10 < peso < 30:
                    return 60
                else:
                    return 70
        except ValueError: #tratamento de erro para caso o usuário não digite um valor numérico
            print('Você digitou um valor não numérico.')
            print('Por favor, digite um número válido.')
            print('')
            continue
    
    
#-----início da função cachorro_pelo()
def cachorro_pelo():
    while True:
        pelo = input('''Entre com o pelo do cachorro:
c - pelo curto
m - pelo médio
l - pelo longo
>>> ''').lower().strip() #altera para minúsculas e elimina possíveis espaços em branco digitados pelo usuário
        print('')
        if pelo not in 'cml':
            print('Opção inválida. Digite novamente.')
            continue #retorna para o início do loop caso o usuário não digite uma opção válida
        else:
            if pelo == 'c':
               return 1
            elif pelo == 'm':
               return 1.5
            else:
               return 2
            
#-----início da função cachorro_extra()
def cachorro_extra():
    adicional = 0 #variável contadora para ir somando os serviços adicionais solicitados pelo usuário
    while True:
        extra = input('''Deseja adicionar mais algum serviço? 
1 - corte de unhas - R$10
2 - escovar dentes - R$12
3 - limpeza de orelhas - R$15
0 - não desejo mais nada
>>> ''')
        print('')
        if extra not in ('1', '2', '3', '0'):
            print('Opção inválida. Digite novamente sua escolha.')
            continue #retorna para o início do loop caso o usuário não digite uma opção válida
        else:
            if extra == '1':
                adicional += 10
            elif extra == '2':
                adicional += 12
            elif extra == '3':
                adicional += 15
            else:
                return adicional
                

#-----início do Main
print('-'*5, 'Bem-vinda(o) ao Petshop da Amanda de Lima Santana!', '-'*5)
base = cachorro_peso() #chama a função cachorro_peso() e guarda seu resultado
multiplicador = cachorro_pelo() #chama a função cachorro_pelo() e recebe seu resultado
adicional = cachorro_extra() #chama a função cachorro_extra() e recebe seu resultado
total = base * multiplicador + adicional #cálculo do valor total

print(f'Total a pagar: R$ {total:.2f} (peso: {base} * pelo: {multiplicador} + adicional(is): {adicional})')