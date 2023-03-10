# Exemplo de menu

print("1 - Cadastro")
print("2 - Consulta")
print("3 - Alteração")
print("4 Exclussão")
print("0 - sair")

opcao = float(input("Digite uma opção:"))

if opcao == 1:
    print("Executando o cadastro ...")
elif opcao == 2:
    print("Executando a consulta")
elif opcao == 3:
    print("Executando a alteração")
elif opcao == 4:
    print("Executando a exclussão")
elif opcao == 0:
    print("Saindo")
