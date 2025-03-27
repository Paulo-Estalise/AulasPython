'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:


Até 5 Kg Acima de 5 Kg

File Duplo R$ 4,90 por Kg R$ 5,80 por Kg

Alcatra R$ 5,90 por Kg R$ 6,80 por Kg

Picanha R$ 6,90 por Kg R$ 7,80 por Kg


Para atender a todos os clientes, cada cliente poderá levar apenas
um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se a compra for feita no cartão Tabajara e a quantidade em kg exceder 7 Kg, o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça
o tipo e a quantidade de carne comprada pelo usuário, além da forma de pagamento
(outras formas de pagamento ou cartão Tabajara). Ao final, mostre o valor total a pagar.
'''
tipo_carne = input("Digite o tipo de carne (1 para Filé Duplo, 2 para Alcatra e 3 para Picanha): ")
quantidade_carne = float(input("Digite a quantidade de carne: "))

# Preço normal
preco_file = 5.80
preco_alcatra = 6.80
preco_picanha = 7.80

# Preço promocional
preco_file_com_desconto = 4.90
preco_alcatra_com_desconto = 5.90
preco_picanha_com_desconto = 6.90


if tipo_carne == "1":
    if quantidade_carne > 5:
        conta = preco_file_com_desconto * quantidade_carne
    else:
        conta = preco_file * quantidade_carne
elif tipo_carne == "2":
    if quantidade_carne > 5:
        conta = preco_alcatra_com_desconto * quantidade_carne
    else:
        conta = preco_alcatra * quantidade_carne
elif tipo_carne == "3":
    if quantidade_carne > 5:
        conta = preco_picanha_com_desconto * quantidade_carne
    else:
        conta = preco_picanha * quantidade_carne
else:
    print("Tipo de carne inválido.")
    exit()

print(f"O valor da sua compra eh R$ {conta:.2f}.")


pagamento = input("A compra será feita com o cartão Tabajara? (S/N): ").strip().upper()

# 5% de desconto se a compra for maior que 7Kg feita com cartão Tabajara
if pagamento == "S" and quantidade_carne >= 7:
    desconto = conta * 0.05
    conta -= desconto
    print(f"Total a pagar com desconto: R$ {conta:.2f}")
else:
    print(f"Total a pagar: R$ {conta:.2f}")
