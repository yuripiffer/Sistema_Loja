from Model import modelProduto


def area_Produto():
    while True:
        opcao = input("\n Area de Produtos:\n"
                      "1 -> Cadastrar categoria de produto\n"
                      "2 -> Excluir categoria de produto\n"
                      "3 -> Cadastrar um novo produto\n"
                      "4 -> Alterar um produto\n"
                      "5 -> Excluir um produto\n"
                      "6 -> Sair\n"
                      " Opção: ")
        if opcao == "1":
            modelProduto.cadastrarCategoria()
        elif opcao == "2":
            modelProduto.deletarCategoria()
        elif opcao == "3":
            modelProduto.cadastrarProduto()
        elif opcao == "4":
            modelProduto.alterarProduto()
        elif opcao == "5":
            modelProduto.deletarProduto()
        elif opcao == "6":
            break
