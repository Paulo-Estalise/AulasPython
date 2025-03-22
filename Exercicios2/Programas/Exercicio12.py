'''
Uma frutaria está vendendo frutas com a seguinte tabela de preços:
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
quantidade_maca = float(input("Digite a quantidade de maças em quilos: "))
quantidade_morango = float(input("Digite a quantidade de morangos em quilos: "))

#maças
if quantidade_maca < 5:
    preco_maca = quantidade_maca * 1.80
elif quantidade_maca >= 5 and quantidade_maca < 8:
    preco_maca = quantidade_maca * 1.50
else:
    preco_maca = quantidade_maca * 1.50 * 0.10

#morangos
if quantidade_morango < 5:
    preco_morango = quantidade_morango * 2.50
elif quantidade_morango >= 5 and quantidade_morango < 8:
    preco_morango = quantidade_morango * 2.20
else:
    preco_morango = quantidade_morango * 2.20

total = preco_maca + preco_morango

if (quantidade_maca + quantidade_morango) > 8 or total > 25:
    desconto = total * 0.10
else:
    desconto = 0


valor_com_desconto = total - desconto

print(f"O valor total a ser pago é: R$ {valor_com_desconto:.2f}")
