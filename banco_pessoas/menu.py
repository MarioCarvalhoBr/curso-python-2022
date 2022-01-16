def menu():
    print ("""
            AGENDA DE CONTATOS
            Opções disponíveis: 
            (1) Inserir contato:
            (2) Deletar:
            (3) Mostrar agenda:
            (4) Buscar contato(cpf):
            (5) Salvar e sair:""")

    opcao = int(input("Digite sua opção: "))
    return opcao