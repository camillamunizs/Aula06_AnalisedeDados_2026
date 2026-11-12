venda = float(input('Digite o valor da venda: R$ '))

match venda:
    case venda if venda < 100:
        print('Venda pequena!')

    case venda if venda < 500:
        print('Venda média!')

    case _:
        print('Venda grande!')