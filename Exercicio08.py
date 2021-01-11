# Feito por: Ronyeri Marinho
#
# QUESTÃO 08 - Implemente um programa que lê como entrada o preço de um produto e o código relativo à forma de pagamento. 
# De acordo com a tabela dada abaixo, deve ser aplicado o desconto especificado e o programa deve exibir o
# número de prestações e o valor de cada prestação a ser paga:
#
# Pagamento:    Código:     desconto:
# À vista         1            30%
# 2 vezes         2            20%
# 3 vezes         3            10%
# 4 a 6 x         4         Sem desconto

dadosPagamento = [["À vista", 1, 30], ["2x", 2, 20], ["3x", 3, 10], ["4 à 6x", 4, 0]]
precoProduto = float(input("Digite o valor do produto: "))
codigoProduto = int(input("Digite o código relativo à forma de pagamento: "))

if codigoProduto == dadosPagamento[0][1]:
    desconto = (precoProduto * dadosPagamento[0][2]) / 100
    valorFinal = precoProduto - desconto
    print("Forma de Pagamento: ", dadosPagamento[0][0])
    print("Preço do Produto: R$", precoProduto)
    print("Desconto: R$", desconto)
    print("VALOR FINAL: R$", valorFinal)

elif codigoProduto == dadosPagamento[1][1]:
    desconto = (precoProduto * dadosPagamento[1][2]) / 100
    valorFinal = precoProduto - desconto
    valorParcelas = valorFinal / dadosPagamento[1][1]
    print("Forma de Pagamento: ", dadosPagamento[1][0])
    print("Preço do Produto: R$", precoProduto)
    print("Desconto: R$", desconto)
    print("Valor por parcela: R$", valorParcelas)
    print("VALOR FINAL: R$", valorFinal)

elif codigoProduto == dadosPagamento[2][1]:
    desconto = (precoProduto * dadosPagamento[2][2]) / 100
    valorFinal = precoProduto - desconto
    valorParcelas = valorFinal / dadosPagamento[2][1]
    print("Forma de Pagamento: ", dadosPagamento[2][0])
    print("Preço do Produto: R$", precoProduto)
    print("Desconto: R$", desconto)
    print("Valor por parcela: R$", valorParcelas)
    print("VALOR FINAL: R$", valorFinal)

elif codigoProduto == dadosPagamento[3][1]:
    quantidadeParcelas = int(input("Digite a quantidade de parcelas desejada: (4 à 6) "))
    valorParcelas = precoProduto / quantidadeParcelas
    print("Forma de Pagamento: ", dadosPagamento[3][0])
    print("Quantidade de parcelas escolhida: ", quantidadeParcelas)
    print("Valor por parcela: R$", round(valorParcelas, 2))
    print("Preço do Produto: R$", precoProduto)

else: 
    print("Código relativo á forma de pagamento inválida!!")
    