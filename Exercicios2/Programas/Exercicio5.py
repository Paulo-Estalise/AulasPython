'''Escreva um algoritmo que solicite um número inteiro e verifique se ele é ou não divisível por 5.'''
num = int(input("Digite um numero: "))  # Usando input() e convertendo para inteiro
if num % 5 == 0:
    print("O número é divisível por 5")
else:
    print("O número não é divisível por 5")
