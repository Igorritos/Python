#1. Calcule o dobro de um numero dado pelo usuário
from builtins import float

# O número
n1 = input("Digite um número: ")
n1 = float(n1)

# Mostrar o dobro

print("O dobro de ", n1, "é ", n1 * 2)


# 2. Calcular a média de tres numeros dados pelo usuário


# Primeiro número
m1 = input("Digite o primeiro número: ")
n1 = float(n1)

# Segundo número
n2 = input("Digite o segundo número: ")
n2 = float(n2)


# Terceito número
n3 = input("Digite o terceito número: ")
n3 = float(n3)


# Calculo da médio entre os 3

med = (n1 + n2 + n3) / 3

# Mostrar a média

print("A média de ", n1, ",", n2, "e ", n3, "é: ", med)


# 3. Dados dois numeros, exibir a soma, subtração, multiplicação e divisão.

# Primeiro número
n1 = input("Digite o primeiro número: ")
n1 = float(n1)

n2 = input("Digite o segundo número: ")
n2 = float(n2)

print("A soma de ", n1, " com", n2, "é ", n1 + n2)
print("A subtração de ", n1, " com", n2, "é ", n1 - n2)
print("A multiplicação de ", n1, " com", n2, "é ", n1 * n2)
print("A divisão de ", n1, " com", n2, "é ", n1 / n2)