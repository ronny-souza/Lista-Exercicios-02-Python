#
# Feito por: Ronyeri Marinho 
#
# QUESTÃO 05 - Um vendedor precisa de um algoritmo que calcule o preço total devido por
# um cliente. O algoritmo deve receber o código de um produto e a quantidade
# comprada e calcular o preço total, usando a tabela abaixo.
#
# Código Preço Unitário
# 'ABCD' R$ 5,30
# 'XYPK' R$ 6,00
# 'KLMP' R$ 3,20
# 'QRST' R$ 2,50

codigo = input("Digite o código do produto: ")
quantidadeComprada = int(input("Digite a quantidade comprada: "))

produtos = [["ABCD", 5.30], ["XYPK", 6.00], ["KLMP", 3.20], ["QRST", 2.50]]

# usando o lower() para tornar ambas em minúsculas para não haver problemas se 
# o usuário digitar maiúsculas ou minúsculas
if codigo.lower() == produtos[0][0].lower():
    total = produtos[0][1] * quantidadeComprada
    print("TOTAL: R$", round(total, 3))

elif codigo.lower() == produtos[1][0].lower():
    total = produtos[1][1] * quantidadeComprada
    print("TOTAL: R$", total)

elif codigo.lower() == produtos[2][0].lower():
    total = produtos[2][1] * quantidadeComprada
    print("TOTAL: R$", total)

elif codigo.lower() == produtos[3][0].lower():
    total = produtos[3][1] * quantidadeComprada
    print("TOTAL: R$", total)

else:
    print("Código digitado é inválido!!")

