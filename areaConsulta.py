import cliente
import areaProduto

def area_Consulta():
    opcao = "0"
    while opcao != "5":
        opcao = input("\n Área de consultas:\n"
                        "1 -> Consultar clientes\n"
                        "2 -> Consultar produtos\n"
                        "3 -> Consultar categorias\n"
                        "4 -> Consultar histórico de vendas\n"
                        "5 -> Sair\n"
                        " Opção: ")
        if opcao == "1":
            cliente.consulta_Cliente()
        elif opcao == "2":
            areaProduto.listarProdutos()
        elif opcao == "3":
            areaProduto.listarCategorias()
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
