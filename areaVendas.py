import pandas as pd
import Pagamento
import areaProduto

def vender_Produtos():
    opcao = "0"
    listaProduto = []
    produtosCadastrados = pd.read_csv("Produto.csv", delimiter=";")
    while opcao != "4":
        opcao = input("\n Menu de vendas:\n"
                      "1 -> Adicionar produto\n"
                      "2 -> Cancelar produto\n"
                      "3 -> Finalizar compra\n"
                      "4 -> Cancelar compra\n"
                      " Opção: ")
        if opcao == "1":
            areaProduto.listarProdutos()
            adicionarProduto = input(" Código do produto: ")
            if len(adicionarProduto) == 4 and adicionarProduto in produtosCadastrados["Codigo_Produto"].to_string():
                listaProduto.append(adicionarProduto)
                print(listaProduto)
            else:
                print("Produto não cadastrado ...")
        elif opcao == "2":
            produtosCadastrados.set_index("Codigo_Produto")
            if len(listaProduto) < 1:
                print("\n Não há produtos no carrinho ...")
            else:
                copia = produtosCadastrados.copy()
                copia.set_index('Codigo_Produto', inplace=True)
                print("\n")
                for i in range(len(listaProduto)):
                    print(f"{listaProduto[i]}\t{copia.loc[[listaProduto[i]],['Nome_Produto']].values[0][0]}\t"
                            f"{copia.loc[[listaProduto[i]],['Categoria_Produto']].values[0][0]}\t"
                               f"{copia.loc[[listaProduto[i]],['Preco']].values[0][0]}")
                removerProduto = input("\n Digite o código do produto que deseja remover: ")
                if removerProduto in listaProduto:
                    print("Produto removido !!")
                    listaProduto.pop(listaProduto.index(removerProduto))
                else:
                    print("Código de produto não encontrado ...")
        elif opcao == "3":
            if len(listaProduto) < 1:
                print("\n Não há produtos no carrinho ...")
            else:
                copia = produtosCadastrados.copy()
                copia.set_index('Codigo_Produto', inplace=True)
                print("\n Carrinho de compras: ")
                for i in range(len(listaProduto)):
                    print(f"{listaProduto[i]}\t{copia.loc[[listaProduto[i]], ['Nome_Produto']].values[0][0]}\t"
                      f"{copia.loc[[listaProduto[i]], ['Categoria_Produto']].values[0][0]}\t"
                      f"{copia.loc[[listaProduto[i]], ['Preco']].values[0][0]}")
                Pagamento.pagamento(listaProduto)
                break
        elif opcao == "4":
            pass
