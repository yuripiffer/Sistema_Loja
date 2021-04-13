from Model import modelCliente, modelPagamento, modelProduto


def area_Consulta():
    while True:
        opcao = input("\n Área de consultas:\n"
                      "1 -> Consultar clientes\n"
                      "2 -> Consultar produtos\n"
                      "3 -> Consultar categorias\n"
                      "4 -> Consultar histórico de vendas\n"
                      "5 -> Sair\n"
                      " Opção: ")
        if opcao == "1":
            modelCliente.consulta_Cliente()
        elif opcao == "2":
            modelProduto.listarProdutos()
        elif opcao == "3":
            modelProduto.listarCategorias()
        elif opcao == "4":
            modelPagamento.consultarHistoricoCompra()
        elif opcao == "5":
            break
