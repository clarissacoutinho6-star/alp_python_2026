usuarios = []

while True:


    print("############################################")
    print("     SISTEMA DE CADASTRO DE USUÁRIOS (TEXTO)")
    print("############################################")

    print()
    print("=== LOGIN ===")

    usuario = input("Login: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":

        print("Login realizado com sucesso! Bem-vindo,", usuario)
        input("\nENTER para continuar...")

        while True:

            print("\n")
            print("############################################")
            print("     SISTEMA DE CADASTRO DE USUÁRIOS (TEXTO)")
            print("############################################")

            print()
            print("=== MENU PRINCIPAL ===")
            print("Usuário logado:", usuario)
            print("1 - Inserir usuário")
            print("2 - Pesquisar usuário")
            print("3 - Remover usuário")
            print("4 - Listar todos os usuários")
            print("5 - Logout")
            print("6 - Encerrar")

            opcao = int(input("Escolha uma opção: "))


            if opcao  == 1:
                nome=input("Digite o nome do usuário: ")
                usuarios.append(nome)
                print(f"Usuário {nome} cadastrado!")


            elif opcao == 2:
                procurar_por = "admin"
                if procurar_por in usuario:
                    indice = usuario.index(procurar_por)
                    print(f"{procurar_por} está no índice {indice}.")
                else:
                    print(f"{procurar_por} não está na lista. ")


            elif opcao == 3:  
             nome = input("Digite o nome do usuário que deseja remover: ")
             if nome in usuarios:
                usuarios.remove(nome)
                print("Usuário removido com sucesso!")

             else:
                print("Usuário não encontrado!")

            
            elif opcao == 4:
                print("\n Lista de usuários" )
                if usuarios == []:
                    print("Nenhum usuário cadastrado!")
                else:
                    for nome in usuarios: 
                        print(nome)
           
            elif opcao == 5:
                print("Fazendo logout...")
                break

            elif opcao == 6:
                print("Programa encerrado!")
                exit()

    else:
        print("Login ou senha incorretos!")
