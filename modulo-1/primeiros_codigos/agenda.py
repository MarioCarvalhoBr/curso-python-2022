lista = []

arq2 = open("agenda.csv","a+")
lista = arq2.readlines()
arq2.close()

def menu():
    print ("\n", "=" * 50) 
    print ("""\nAGENDA ELETRONICA\n\n
             escolha a opcao: \n
             (1) Inserir contato:\n
             (2) Deletar:\n
             (3) Mostrar agenda:\n
             (4) finalizar programa:\n""")

def lista_agenda(nome, data, opc):

    if( opc == 1):
        contato = nome + ";" + data + "\n" #concatenao o 'nome' ';' e 'data'
        lista.append(contato)
        lista.sort() #ordena a lista por prioridade

    elif (opc == 2):
        print ("=" * 30)
        if ( lista == []): #se lista for vazia
            print ("Lista Vazia\n")
        else:
            lista.pop(0)#remove o elemento de maior prioridade, ou seja, indice 0 da lista
            print ("Removido o elemento de maior prioridade")
        print ("=" * 30)

    elif (opc == 3):
        print ("=" * 30)
        if (lista == []):
            print ("Lista vazia!")
        else:
            print ("Nome:   | Data:")
            for i in lista:
                print (i)
        print ("=" * 30)

    elif (opc == 4):
        arq = open("agenda.csv","w") #escreve por cima do arquivo antigo (atualiza lista)
        tam = len(lista) #recebe o tamanho da lista
        #for que insere os valores no arquivo separado por ';' sendo nome = indice par e data = impar

        for i in range(tam):
            arq.write(lista[i])

        arq.close()

opc = 0 #variavel pro menu

while (opc != 4 ):

    menu() #chama o menu

    while True:
        try:
            opc = int(input(': ')) #recebe a op��o
            break
        except:
            print ("digite s� numeros v�lidos")

    if ( opc == 1 ):
        print ("Informe o nome do contato: \n")
        nome = input(': ')

        print ("informe a data de nascimento: \n")
        data = input(': ')

        lista_agenda(nome, data, 1) #chama a fun��o para inserir na lista

    elif ( opc == 2):
        lista_agenda(0,0,2) #chama a fun��o para deletar o nome na lista

    elif (opc == 3): #chama a fun��o para mostrar na tela
        print ("Lista de contatos: ")
        lista_agenda(0,0,3)
                
lista_agenda(0,0,4) #grava a lista na agenda
print ("FIM DO PROGRAMA! ")

    
