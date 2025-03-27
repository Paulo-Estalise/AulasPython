'''
Um grupo de amigos resolveu fazer um happy hour em um bar após o horário de trabalho.
 Na ocasião eles pediram porções de batatas fritas, pastéis e cervejas para acompanhar.
 Escreva um programa em Python que calcule o total do pedido baseado nas quantidades de
 porções e cervejas consumidas tendo como referência a tabela abaixo. Além disso, calcule
 o valor individual da conta de acordo com o número de amigos.
'''
pessoas = int(input("Digite a quantidade de pessoas: "))
batatas = int(input("Digite a quantidade de porções de batatas: "))
pasteis = int(input("Digite a quantidade de porções de pasteis: "))
cervejas = int(input("Digite a quantidade de cervejas: "))
#calcular
total_batatas = batatas * 35
total_pasteis = pasteis * 25
total_cervejas = cervejas * 18
valor_total = (total_batatas + total_pasteis + total_cervejas) / pessoas
print(f"O valor por pessoa é R$ {valor_total:.2f}")