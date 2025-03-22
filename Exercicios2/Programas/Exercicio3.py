'''Escreva um algoritmo que solicite o valor de uma mercadoria e qual o valor que o
usuário tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria.'''
valor_mercadaria = float(input("Digite valor da mercadoria: "))
dinheiro_comprador = float(input("Digite dinheiro comprador: "))
if valor_mercadaria > dinheiro_comprador: print(f"Compra negada!")
elif valor_mercadaria <= dinheiro_comprador: print(f"Compra Aprovada!")
