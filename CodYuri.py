import pandas as pd
import uuid
#
# prod = pd.read_csv("Produtosdsds.csv", delimiter = ";")
# df = pd.DataFrame(prod)
# print(df)
# # print(df["Nome_Produto"])


def cadastrarCategoria():
    novaCategoria = input("Insira um nova categoria de produto:")
    with open("Categoria.txt", "a") as f:
        input_dado = f"{novaCategoria}\n"
        f.write(input_dado)
    # EXTRA
    #Checar se o usuário gostaria de listar todas as categorias
        #chamar a função de listar categorias


def cadastrarProduto():
    nomeProduto = input("Cadastre o nome do produto:")
    idProduto = str(uuid.uuid4())[0:4]
    categoriaProduto = inputCategoria()
    precoProduto = input("Insira o preço do produto {}:".format(nomeProduto))
    # questões relacionadas a vírgulas etc

    with open("Produto.csv", "a") as f:
        input_dado = f"{idProduto};{nomeProduto};{categoriaProduto};{precoProduto}\n"
        f.write(input_dado)

def inputCategoria():
    with open("Categoria.csv", "r") as f:
        Categorias = f.read()
        print("CATEGORIAS DISPONÍVEIS:")
        print(Categorias)
        categoriaProduto = input("Insira a categoria do produto: ")
        while categoriaProduto not in Categorias:
            print("Categoria não encontrada.")
            categoriaProduto = input("Insira a categoria do produto: ")
    return categoriaProduto

def listarCategorias():
    with open("Categoria.csv", "r") as f:
        print(f.read())


def listarProdutos():
    Produtos = pd.read_csv("Produto.csv", delimiter=";")
    print(Produtos)

#df[["Categoria_produto"],["e15d"]]

def alterarProduto():
    df = pd.read_csv("Produto.csv", delimiter = ";")
    df.set_index('Codigo_Produto', inplace= True)

    codigoProduto = input("Insira o código do produto a ser alterado:")
    while codigoProduto not in df.index:       #["Codigo_Produto"].to_string():
        print("Código não encontrado.")
        codigoProduto = input("Insira o código do produto a ser alterado:")

    opcao = 0
    while opcao not in [1, 2, 3]:
        opcao = int(input(""" Insira um dos números abaixo:
        1 - para alterar o nome do produto,
        2 - para alterar a categoria do produto,
        3 - para alterar o preço do produto."""))
        if opcao == 1:
            print(f"O antigo nome do produto é {df.loc[[codigoProduto],['Nome_Produto']].values}.")
            novoNomeProduto = input("Insira o novo nome para o produto:")
            df.loc[[codigoProduto],['Nome_Produto']] = novoNomeProduto
            df.to_csv("Produto.csv", sep = ";")
            print(f"O novo nome do produto é {df.loc[[codigoProduto], ['Nome_Produto']].values}.")

        elif opcao == 2:
            print(f"O antigo nome do produto é {df.loc[[codigoProduto],['Categoria_Produto']].values}.")
            categoriaProduto = inputCategoria()
            df.loc[[codigoProduto], ['Categoria_Produto']] = categoriaProduto
            df.to_csv("Produto.csv", sep = ";")
            print(f"A nova categoria do produto é {df.loc[[codigoProduto], ['Categoria_Produto']].values}.")
        elif opcao == 3:
            print(f"O antigo preço do produto é {df.loc[[codigoProduto],['Preco']].values}.")
            novoPrecoProduto = input("Insira o novo preço para o produto:")
            df.loc[[codigoProduto],['Preco']] = novoPrecoProduto
            df.to_csv("Produto.csv", sep = ";")
            print(f"O novo preço do produto é {df.loc[[codigoProduto], ['Preco']].values}.")
        else:
            print("Opção inexistente!")



def deletarProduto():
    df = pd.read_csv("Produto.csv", delimiter = ";")
    df.set_index('Codigo_Produto', inplace= True)
    codigoProduto = input("Insira o código do produto a ser deletado:")
    while codigoProduto not in df.index:
        print("Código não encontrado.")
        codigoProduto = input("Insira o código do produto a ser deletado:")
    df.drop(codigoProduto, inplace = True)
    df.to_csv("Produto.csv", sep=";")
    #printar o que foi deletado.

def deletarCategoria():
    df = pd.read_csv("Categoria.csv", delimiter = ";")
    print("CATEGORIAS DISPONÍVEIS:")
    print(df)
    #CHECAR SE A CATEGORIA EXISTE --. BOTAR UM WHILE
    delCategoria = input("Insira o nome da categoria a ser deletada:")
    df.replace( delCategoria, "None", inplace = True)
    df.to_csv("Categoria.csv", sep=";", index=False)



deletarCategoria()
#cadastrar
# Produto()
#listarProdutos()

# df = pd.read_csv("Produto.csv", delimiter = ";")
# df.set_index('Codigo_Produto', inplace= True)
# #print(df.loc[["3"],["Nome_Produto"]])

#print(df.loc[["3"],['Nome_Produto']].values)