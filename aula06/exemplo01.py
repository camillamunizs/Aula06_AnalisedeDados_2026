compra = float(input('Digite o valor da compra: R$ '))


print('''
[1] - PIX (12% de Desconto)
[2] - DÉBITO (8% de Desconto)
[3] - CRÉDITO (5% de Desconto)
[4] - DINHEIRO (15% de Desconto)
''')

desconto = 0
opcao =  int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
        print('---- PIX ----')
        desconto = compra * 0.12


    case 2:
        print('---- DÉBITO ----')
        desconto = compra * 0.08


    case 3:
        print('---- CRÉDITO ----')
        desconto = compra * 0.05


    case 4:
        print('---- DINHEIRO ----')
        desconto = compra * 0.15

    case _:
        print('Opção inválida')

if desconto != 0:
    valor_final = compra - desconto 
    print(f'Valor total: R$ {compra}')
    print(f'Desconto: R$ {compra}')
    print(f'Total a pagar: R$ {valor_final}')

else: 
    print('Por favor, escolha uma das opções acima')

    
    
