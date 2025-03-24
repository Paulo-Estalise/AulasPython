'''
Uma frutaria está vendendo frutas com a seguinte tabela de preços:
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
quantidade_maca = float(input("Digite a quantidade de maçãs em quilos: "))
quantidade_morango = float(input("Digite a quantidade de morangos em quilos: "))

if quantidade_maca <= 5:
    preco_maca = quantidade_maca * 1.80
else:
    preco_maca = quantidade_maca * 1.50

if quantidade_morango <= 5:
    preco_morango = quantidade_morango * 2.50
else:
    preco_morango = quantidade_morango * 2.20

total = preco_maca + preco_morango

if (quantidade_maca + quantidade_morango) > 8 or total > 25:
    total *= 0.9

print(f"O valor total a ser pago é: R$ {total:.2f}")

