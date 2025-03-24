'''Escreva um algoritmo que solicite o valor de uma mercadoria e qual o valor que o
usuário tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria.'''
valor_mercadoria = float(input("Digite o valor da mercadoria: "))
dinheiro_comprador = float(input("Digite o dinheiro do comprador: "))

if valor_mercadoria <= dinheiro_comprador:
    print("Compra Aprovada!")
else:
    print("Compra Negada!")

