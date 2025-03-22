'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva
um programa que solicite o número de maçãs compradas, calcule e escreva o custo total da compra.
'''

quant = int(input("Digite a quantidade de maçãs compradas: "))
if quant <= 11:
    conta = quant * 1.30
else:
    conta = quant * 1.00

print(f"O valor é R$: {conta:.2f}")

