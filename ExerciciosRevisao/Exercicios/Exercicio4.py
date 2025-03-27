'''
A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar
 mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo
de 50%.  Escreva um algoritmo que solicite o número de horas trabalhadas em um mês,
o salário por  hora e escreva o salário total do funcionário, que deverá ser acrescido das
horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

'''
'''valor_hora = int(input("Digite o valor da hora: "))
quantidade_horas = int(input("Digite a quantidade de horas trabalhadas: "))
if quantidade_horas >= 40:
    print(f"O valor do salario eh R$ {valor_hora * quantidade_horas * 4:.2f}")
elif quantidade_horas <= 40:
    print(f"O valor do salario eh R$ {valor_hora * quantidade_horas * 0.50 * 4:.2f}")
'''
valor_hora = float(input("Digite o valor da hora: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

horas_regulares = 160
if quantidade_horas >= horas_regulares:
    horas_extras = quantidade_horas - horas_regulares
    salario = (horas_regulares * valor_hora) + (horas_extras * valor_hora * 1.5)
else:
    salario = quantidade_horas * valor_hora

print(f"O salário total é R$ {salario:.2f}")
