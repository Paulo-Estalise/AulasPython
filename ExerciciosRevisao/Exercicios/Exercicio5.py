'''

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

- Álcool:

- até 20 litros, desconto de 3% por litro

- acima de 20 litros, desconto de 5% por litro

- Gasolina:

- até 20 litros, desconto de 4% por litro

- acima de 20 litros, desconto de 6% por litro

- Diesel:

- até 20 litros, desconto de 2% por litro

- acima de 20 litros, desconto de 7% por litro


Escreva um programa em Python que solicite ao usuário o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina ou D-Diesel),
 calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
da gasolina é R$ 6,09, o preço do litro do álcool é R$ 4,04 e o preço do litro
do Diesel é R$ 5,93.

'''

preco_alcool = 4.04
preco_gasolina = 6.09
preco_diesel = 5.93

tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina, D para Diesel): ").upper()
quantidade_litros = float(input("Digite a quantidade de litros: "))


if tipo_combustivel == "A":
    preco_por_litro = preco_alcool
    desconto = 0.03 if quantidade_litros <= 20 else 0.05
elif tipo_combustivel == "G":
    preco_por_litro = preco_gasolina
    desconto = 0.04 if quantidade_litros <= 20 else 0.06
elif tipo_combustivel == "D":
    preco_por_litro = preco_diesel
    desconto = 0.02 if quantidade_litros <= 20 else 0.07
else:
    print("Opção inválida! Digite A para Álcool, G para Gasolina ou D para Diesel.")
    exit()


valor_bruto = quantidade_litros * preco_por_litro
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

print(f"Valor total a pagar: R$ {valor_final:.2f}")



