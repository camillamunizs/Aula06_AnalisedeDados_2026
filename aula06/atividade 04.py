for i in range (5):
    print(f'\n-------------- COMPRA {i+1} --------------')
    venda = float(input('Informe o valor da venda: R$ '))

    desconto = venda * 0.10
    sem_desconto = venda * 0
   
    if venda >= 200:
        valor_final = venda - desconto
        print(f'Parabéns! Você ganhou R$ {desconto:.2f} desconto! \nTotal a pagar: R$ {valor_final} ')

    else:
        print (f'Total a pagar: R$ {venda:.2f}')
  
    