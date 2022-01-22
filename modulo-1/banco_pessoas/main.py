import menu
import banco

while True:

    opcao = menu.menu()

    if opcao == 1:
        banco.inserir()
    elif opcao == 2:
        cpf = input("Digite o CPF que deseja remover: ")
        banco.remover_contato_cpf(cpf)
    elif opcao == 3:
        banco.listar_agenda()
    elif opcao == 4:
        cpf = input("Digite o CPF que deseja buscar: ")
        banco.buscar_contato_cpf(cpf)
    elif opcao == 5:
        banco.salvar()
        break
    else:
        "Opção inválida!"
