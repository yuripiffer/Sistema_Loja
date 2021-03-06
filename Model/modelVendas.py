from Model import modelProduto
from Model import modelPagamento

def adicionarProduto(listaProduto, produtosCadastrados):
    modelProduto.listarProdutos()
    adicionarProduto = input(" Código do produto: ")
    if len(adicionarProduto) == 4 and adicionarProduto in produtosCadastrados["Codigo_Produto"].to_string():
        listaProduto.append(adicionarProduto)
        print(listaProduto)
    else:
        print("Produto não cadastrado ...")


def cancelarProduto(listaProduto, produtosCadastrados):
    produtosCadastrados.set_index("Codigo_Produto")
    if len(listaProduto) < 1:
        print("\n Não há produtos no carrinho ...")
    else:
        copia = produtosCadastrados.copy()
        copia.set_index('Codigo_Produto', inplace=True)
        print("\n")
        for i in range(len(listaProduto)):
            print(f"{listaProduto[i]}\t{copia.loc[[listaProduto[i]], ['Nome_Produto']].values[0][0]}\t"
                  f"{copia.loc[[listaProduto[i]], ['Categoria_Produto']].values[0][0]}\t"
                  f"{copia.loc[[listaProduto[i]], ['Preco']].values[0][0]}")
        removerProduto = input("\n Digite o código do produto que deseja remover: ")
        if removerProduto in listaProduto:
            print("Produto removido !!")
            listaProduto.pop(listaProduto.index(removerProduto))
        else:
            print("Código de produto não encontrado ...")


def finalizarCompra(listaProduto, produtosCadastrados):
    if len(listaProduto) < 1:
        print("\n Não há produtos no carrinho ...")
    else:
        copia = produtosCadastrados.copy()
        copia.set_index('Codigo_Produto', inplace=True)
        print("--------------------------------")
        print(" Carrinho de compras:\n ")
        for i in range(len(listaProduto)):
            print(f"{listaProduto[i]}\t{copia.loc[[listaProduto[i]], ['Nome_Produto']].values[0][0]}\t"
                  f"{copia.loc[[listaProduto[i]], ['Categoria_Produto']].values[0][0]}\t"
                  f"{copia.loc[[listaProduto[i]], ['Preco']].values[0][0]}")
        print("--------------------------------")
        modelPagamento.pagamento(listaProduto)
