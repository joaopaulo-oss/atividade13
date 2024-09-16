# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zer
número = int(input("digite um número:")) 

if número >= 0:
    print("positivo")

elif número <= 0:
    print("negativo")

elif número == 0:
    print("zero")