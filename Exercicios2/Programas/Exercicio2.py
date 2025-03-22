'''
Um condomínio possui 20 blocos e para uma correta administração possui dois síndicos: o sr José que administra
os blocos de 1 a 10 e o sr Hamilton que administra os blocos de 11 a 20.
Escreva um algoritmo que solicite ao usuário em qual bloco ele mora e escreva na tela qual o síndico responsável.
'''
bloco = int(input("Em qual bloco você mora? (1-20): "))
if 1 <= bloco <= 10:
    print("O síndico responsável pelo seu bloco é o Sr. José.")
elif 11 <= bloco <= 20:
    print("O síndico responsável pelo seu bloco é o Sr. Hamilton.")
else:
    print("Bloco inválido! Digite um número entre 1 e 20.")

