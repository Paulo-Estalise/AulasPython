'''Uma livraria resolveu fazer uma promoção, com os seguintes critérios:

o Livros com preços até R$ 10,00 - desconto de 8%

o Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%

o Livros com preços acima de R$ 60,00 - desconto de 20%

Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto oferecido, em reais.'''


valor_livro = float(input("Digite o valor do livro: "))
if valor_livro <= 10:
    desconto = valor_livro * 0.08
elif valor_livro <= 60:
    desconto = valor_livro * 0.10
else:
    desconto = valor_livro * 0.20

print(f"O valor do desconto é: R$ {desconto:.2f}")


