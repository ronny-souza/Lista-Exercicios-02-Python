# Feito por: Ronyeri Marinho
# 
# QUESTÃO 03 - Escreva um programa que leia o valor dos 3 ângulos de um triângulo e escreva se 
# o triângulo é Acutângulo Retângulo ou Obtusângulo.
# Sendo que:
# − Triângulo Retângulo: possui um ângulo reto (igual a 90o)
# − Triângulo Obtusângulo: possui um ângulo obtuso (maior que 90o)
# − Triângulo Acutângulo: possui três ângulos agudos (menores que 90o)

anguloUm = float(input("Digite o primeiro ângulo: "))
anguloDois = float(input("Digite o segundo ângulo: "))
anguloTres = float(input("Digite o terceiro ângulo: "))

if anguloUm == 90.0 or anguloDois == 90.0 or anguloTres == 90.0:
    print("Trata-se de um Triângulo Retângulo!")

elif anguloUm > 90.0 or anguloDois > 90.0 or anguloTres > 90.0:
    print("Trata-se de um Triângulo Obtusângulo!")

else:
    print("Trata-se de um Triângulo Acutângulo!")

