# Feito por: Ronyeri Marinho 
#
# QUESTÃO 07 - Crie um programa que receba as três notas de um aluno e calcule a média
# aritmética entre elas. Após o cálculo da média, trate as seguintes situações:
# a) Se a média for maior que 6, o aluno é Aprovado por Média
# b) Se a média for menor que 6 e maior ou igual a 4, o aluno tem status
# Exame Final
# c) Se a média for menor que 4, o aluno é Reprovado.

notas = [0.0, 0.0, 0.0]
somaNotas = 0.0

for n in range(3):
    #n += 1 pois senão iria imprimir digite a 0º nota do aluno, visto que é um array
    notas[n] = float(input("Digite a {n}º nota do aluno: ".format(n = n + 1)))


for n in range(3):
    somaNotas += notas[n]

media = somaNotas / len(notas)

if media >= 6.0 and media <= 10.0: 
    print("MÉDIA: ", round(media, 1))
    print("STATUS: APROVADO!")

elif media < 6.0 and media > 4.0:
    print("MÉDIA: ", round(media, 1))
    print("STATUS: EXAME FINAL!")

else: 
    print("MÉDIA: ", round(media, 1))
    print("STATUS: REPROVADO!")