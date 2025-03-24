'''Faça um programa que solicite dois números e execute as operações listadas a

seguir de acordo com a escolha do usuário:'''
from unittest import case

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print("\nEscolha uma operação:")
print("1 - Média dos números")
print("2 - Maior número")
print("3 - Menor número")
print("4 - Divisão inteira dos numeros digitados")
calculos = int(input("\nDigite o número da operação desejada: "))
def operacoes(num1, num2, calculos):
    match calculos:
        case 1:
            resultado = (num1 + num2) / 2
            print(f"Média dos números: {resultado:.2f}")
        case 2:
            resultado = max(num1, num2)
            print(f"Maior número: {resultado}")
        case 3:
            resultado = min(num1, num2)
            print(f"Menor número: {resultado}")
        case 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Divisão: {resultado:.2f}")
            else:
                print("Erro: Divisão por zero não é permitida!")
        case _:
            print("Opção inválida! Escolha um número entre 1 e 4.")

operacoes(num1, num2, calculos)