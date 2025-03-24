'''
Um funcionário irá receber um aumento de acordo com o seu plano de trabalho, de acordo com a tabela abaixo:
Plano de trabalho Porcentagem de aumento
A 10%
B 15%
C 20%
Faça um programa que leia o plano de trabalho e o salário atual de um funcionário e calcula e imprime o seu novo salário.
'''

salario_atual = float(input("Digite o salário atual do funcionário: "))
plano = input("Digite o plano de trabalho (A, B ou C): ")
def calcular_novo_salario(salario, plano):
    match plano:
        case "A":
            aumento = salario * 0.10
        case "B":
            aumento = salario * 0.15
        case "C":
            aumento = salario * 0.20
        case "a":
            aumento = salario * 0.10
        case "b":
            aumento = salario * 0.15
        case "c":
            aumento = salario * 0.20
        case _:
            print("Plano inválido! Escolha A, B ou C.")
            return

    novo_salario = salario + aumento
    print(f"Novo salário: R$ {novo_salario:.2f}")



calcular_novo_salario(salario_atual, plano)
