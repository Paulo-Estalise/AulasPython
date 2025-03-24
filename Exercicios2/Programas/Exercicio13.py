'''
O cardápio de uma casa de lanches é dado pela tabela abaixo:
Escreva um algoritmo que solicite o código do item adquirido pelo consumidor e a quantidade, calculando e mostrando
o valor a pagar. Não será necessário exibir o produto e o valor, somente o valor final.
OBS: utilize a estrutura de decisão match...case.
'''

codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))


def pedido(codigo, quantidade):
    match codigo:
        case 100:
            preco = 1.70
        case 101:
            preco = 2.30
        case 102:
            preco = 2.60
        case 103:
            preco = 2.40
        case 104:
            preco = 2.50
        case 105:
            preco = 1.00
        case _:
            print("Código inválido!")
            return


    total = preco * quantidade
    print(f"Total a pagar: R$ {total:.2f}")


pedido(codigo, quantidade)

