import cliente

def area_Consulta():
    opcao = "0"
    while opcao != "3":
        opcao = input("\n Área de consultas:\n"
                          "1 -> Consultar clientes\n"
                          "2 -> Consultar histórico de vendas\n"
                          "3 -> Sair\n"
                          " Opção: ")
        if opcao == "1":
            cliente.consulta_Cliente()
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
