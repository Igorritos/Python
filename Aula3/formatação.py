sal = 3575.95
idade = 48

# Forma convencional
print("O seu salário é ", sal, "e você tem ", idade, "anos")

# Forma utilizando o +
print("O seu salário é "+ str(sal) +" e você tem "+ str(idade) +" anos")

# Forma do format primeira forma
print("O seu salário é {} e você tem {} anos".format(sal, idade))

# Forma do format segunda forma
print("O seu salário é {0} e você tem {1} anos".format(sal, idade))


# Forma do format terceira forma
print("O seu salário é {s} e você tem {i} anos".format(s = sal, i = idade))

# Forma o print 'f'
print(f"O seu salário é {sal} e você tem {idade} anos")

# Forma o print 'f' forma 2
print(f"O seu salário é {sal:.4f} e você tem {idade} anos")
print(f"O seu salário é {sal:15.4f} e você tem {idade:05d} anos")