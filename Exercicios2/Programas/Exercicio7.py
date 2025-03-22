'''
Escreva um programa que pergunte ao usuário qual foi a média anual de um aluno e ao final diga se ele está aprovado,
reprovado ou de exame. Considere que o aluno está aprovado caso a média seja maior ou igual a 6.0; de exame
com a média entre 3.0 e 5.9 e reprovado com média menor do que 3.0.
'''

media = float(input("Qual foi a média anual do aluno? "))
if media >= 6.0:
    print("O aluno está aprovado.")
elif 3.0 <= media < 6.0:
    print("O aluno está de exame.")
else:
    print("O aluno está reprovado.")
