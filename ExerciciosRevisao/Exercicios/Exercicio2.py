'''
Desenvolva um programa que solicite a idade de um cliente e informe o preço do
]ingresso de um parque temático de acordo com as seguintes regras:
adultos (18-64 anos) pagam $20,
idosos (65 anos ou mais) pagam $15,
e crianças (menos de 18 anos) pagam $10.
'''
idade = int(input('Digite sua idade: '))

if 18 <= idade <= 64:
    print("O valor a ser pago é R$ 20.00")
elif idade >= 65:
    print("O valor a ser pago é R$ 15.00")
else:
    print("O valor a ser pago é R$ 10.00")

