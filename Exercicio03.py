# Feito por: Ronyeri Marinho
# 
# QUESTÃO 03 - Considere que o último concurso vestibular apresentou três provas:
# Português, Matemática e Conhecimentos Gerais. Considerando que para
# cada candidato tem-se um registro contendo o seu nome e as notas obtidas
# em cada uma das provas, construa um algoritmo que forneça:
# a) o nome e as notas em cada prova do candidato
# b) a média do candidato
# c) uma informação dizendo se o candidato foi aprovado ou não. Considere
# que um candidato é aprovado se sua média for maior que 7.0 e se não
# apresentou nenhuma nota abaixo de 5.0

candidato = input("Digite o nome do candidato: ")
disciplinas = ["Português", "Matemática", "Conhecimentos Gerais"]
notas = []
situacao = ""

for i in range(3):
    notas.append(float(input("Digite a nota: ")))

for x in range(3):
    print("{}: {} ".format(disciplinas[x], notas[x]))

media = ((notas[0] + notas[1] + notas[2]) / len(notas))

print("\n\nCANDIDATO:", candidato)
print("MÉDIA:", media)

# Esta parte do código poderia ser otimizada 
for n in notas:
    notaTemp = n
    if (media > 7.0 and notaTemp < 5.0):
       
       situacao = "APROVADO!!"

    else:
       situacao = "REPROVADO!!"

print("SITUAÇÃO:", situacao)