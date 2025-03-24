'''Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança máxima de R$ 35,00,
independente do número de horas. Escreva um algoritmo que pergunte ao usuário qual foi o período
de permanência em horas e escreva na tela o total a pagar.'''
horas = float(input("Digite o tempo em horas no estacionamento: "))
totalMult = horas * 5
if horas <= 7:
    print(f"O valor a pagar é: R$ {totalMult:.2f}")
else:
    print(f"O valor a pagar é: R$ 35.00")
