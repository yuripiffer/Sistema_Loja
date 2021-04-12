import cliente


def area_Cliente():
    while True:
        opcao = input("\n Área do cliente: \n"
                      "1 -> Cadastrar cliente\n"
                      "2 -> Realizar compra\n"
                      "3 -> Sair\n"
                      " Opção:  ")
        if opcao == "1":
            cliente.cadastro_Cliente()
        elif opcao == "2":
            cliente.area_Vendas_Cliente()
            break
        elif opcao == "3":
            break
