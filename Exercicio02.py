# Feita por: Ronyeri Marinho
#
# QUESTÃO 02 - O sistema de avaliação de determinada disciplina, é composto por três provas.
# A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5.
# Faça um algoritmo para calcular a média final de um aluno desta disciplina.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10)

print("Média Final:", media)