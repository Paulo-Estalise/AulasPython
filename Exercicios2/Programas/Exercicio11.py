'''
Considerando o IMC (índice de massa corpórea), calculado como peso/(altura*altura), exiba a situação da pessoa com base na seguinte tabela:

IMC Situação

<= 18.5 Abaixo do peso

>18.5 e <=24.9 Peso ideal

>24.9 Acima do peso
'''
peso = float(input("Digite o peso da pessoa em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print("Peso ideal")
else:
    print("Acima do peso")
