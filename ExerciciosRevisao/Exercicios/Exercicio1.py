'''
Com a volta das aulas presenciais, a mãe de um aluno do ensino fundamental
necessita saber quanto gastará com material escolar. Para fazer uma simulação,
ela foi a uma livraria com o objetivo de simular a compra dos seguintes itens
 básicos: canetas, lápis e cadernos. Um ponto a se considerar é que essa livraria
 está com um programa de desconto de 20% nos preços dos cadernos e 5% nas canetas.
 Assim sendo, escreva um programa em Python que solicite
as quantidades dos itens, preços e calcule o total da compra simulada.
'''
caneta = int(input('Digite a quantidade de caneta: '))
lapis = int(input('Digite a quantidade de lapis: '))
cadernos = int(input('Digite a quantidade de cadernos: '))
#Aplicando valores dos itens
valor_caneta = int(input('Digite o valor da caneta: '))
valor_lapis = int(input('Digite o vaor do lapis: '))
valor_cadernos = int(input('Digite o valor do caderno: '))
#calculando
caneta_total = (caneta * valor_caneta) * 0.95
lapis_total = lapis * valor_lapis
caderno_total = (cadernos * valor_cadernos) * 0.80
total = caneta_total + lapis_total + caderno_total
print(f"O valor da sua compra eh R$ {total:.2f}")