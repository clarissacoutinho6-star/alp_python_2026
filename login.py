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

            if opcao == 5:
                print("Fazendo logout...")
                break

            elif opcao == 6:
                print("Programa encerrado!")
                exit()

            else:
                print("Essa opção ainda não está funcionando.")

    else:
        print("Login ou senha incorretos!")
