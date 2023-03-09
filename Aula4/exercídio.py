'''
Fazer um programa que peça uma venda do usuário.
Caso a venda seja maio de que 500, dar um desconto de 50 reais
'''

v = float(input("Qual o valor da venda? "))
if v > 500:
    v = v - 50
else:
    v = v - 30
print(v)



'''
Pedir ao usuário o valor da venda e se ele tem cupom ou não, se a venda for maior do que 500 ele
terá um desconto de 12% se não desconto de 6% no valor da venda. Caso o usuário tenha o cupom
será debitado 50 reais da venda com o desconto
'''