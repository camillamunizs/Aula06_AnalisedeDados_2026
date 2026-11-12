valor = float(input('Informe o valor do ingresso: R$ '))

print('''
[1] - Inteira
[2] - Meia entrada (50% de desconto)
[3] - Promoção (30% de desconto)
''')

desconto = 0
entrada = int(input('Informe o tipo de entrada: '))

match entrada:
    case 1:
        print('---- INTEIRA ----')
      

    case 2:
        print('---- MEIA ENTRADA ----')
        desconto = valor * 0.50

    case 3:
        print('---- PROMOÇÃO ----')
        desconto = valor * 0.30

    
    case _:
        print('Erro! Selecione uma opção válida')



if entrada in [1,2,3]:
    valor_final = valor - desconto 
    print(f'Valor total: R$ {valor}')
    print(f'Desconto: R$ {desconto}')
    print(f'Total a pagar: R$ {valor_final}')

else: 
    print('Digie uma das opções acima')

    




    
    

    




