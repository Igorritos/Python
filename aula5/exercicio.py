'''
Pedir ao usuário o valor da venda e se ele tem cupom ou não, se a venda for maior do que 500 ele
terá um desconto de 12% se não desconto de 6% no valor da venda. Caso o usuário tenha o cupom
será debitado 50 reais da venda com o desconto
'''


v = float(input("Qual o valor da venda? "))
c = (input("Você tme cupom? s para SIM ou n pra Nâo: "))


if v > 500:
    v = v - (v * 0.12)
else:
    v = v - (v * 0.06)


if c == "s":
    v = v - 50
print("O seu desconto é ", v)