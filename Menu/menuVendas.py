import pandas as pd
from Model import modelVendas



def vender_Produtos():
    listaProduto = []
    produtosCadastrados = pd.read_csv("../DataBase/Produto.csv", delimiter=";")
    while True:
        opcao = input("\n Menu de vendas:\n"
                      "1 -> Adicionar produto\n"
                      "2 -> Cancelar produto\n"
                      "3 -> Finalizar compra\n"
                      "4 -> Cancelar compra\n"
                      " Opção: ")

        if opcao == "1":
            modelVendas.adicionarProduto()
        elif opcao == "2":
            modelVendas.cancelarProduto()
        elif opcao == "3":
            modelVendas.finalizarCompra()
            break
        elif opcao == "4":
            break
