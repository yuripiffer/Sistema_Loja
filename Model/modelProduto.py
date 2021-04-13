import pandas as pd
import uuid
# import DataBase.DadosCartao.csv


def cadastrarCategoria():
    while True:
        novaCategoria = input("Insira uma nova categoria de produto:")
        if novaCategoria.replace(" ", "") == "" or len(novaCategoria) > 30:
            print("Nome de categoria inválido ...")
        elif novaCategoria in str(pd.read_csv("../DataBase/Categoria.csv", dtype=str)):
            print("Categoria já registrada ...")
        else:
            print("Categoria registrada !!")
            break
    with open("../DataBase/Categoria.csv", "a") as f:
        input_dado = f"{novaCategoria.upper()}\n"
        f.write(input_dado)
        print(f"Categoria {novaCategoria} cadastrada com sucesso.")


def cadastrarProduto():
    while True:
        nomeProduto = input("Cadastre o nome do produto:")
        if nomeProduto.replace(" ", "") == "":
            print("Nome de produto inválido ...")
        else:
            break
    idProduto = str(uuid.uuid4())[0:4]
    categoriaProduto = inputCategoria()
    while True:
        try:
            precoProduto = float(input(f"Insira o preço do produto: {nomeProduto}:").replace(",", "."))
            if precoProduto <= 0:
                raise Exception
        except:
            print("Valor informado é incorreto.")
        else:
            break
    with open("../DataBase/Produto.csv", "a") as f:
        input_dado = f"{idProduto};{nomeProduto};{categoriaProduto};{precoProduto}\n"
        f.write(input_dado)
    print(f"Produto {nomeProduto} cadastrado com sucesso!")


def inputCategoria():
    with open("../DataBase/Categoria.csv", "r") as f:
        Categorias = f.read()
        print("CATEGORIAS DISPONÍVEIS:")
        print(Categorias)
        categoriaProduto = input("Insira a categoria do produto: ")
        while categoriaProduto not in Categorias:
            print("Categoria não encontrada.")
            categoriaProduto = input("Insira a categoria do produto: ")
    return categoriaProduto


def listarCategorias():
    with open("../DataBase/Categoria.csv", "r") as f:
        print(f.read())


def listarProdutos():
    Produtos = pd.read_csv("../DataBase/Produto.csv", delimiter=";")
    print(Produtos)


def alterarProduto():
    df = pd.read_csv("../DataBase/Produto.csv", delimiter=";")
    df.set_index('Codigo_Produto', inplace=True)
    print("------------------------------------------------------")
    print(df)
    print("------------------------------------------------------")
    codigoProduto = input("Insira o código do produto a ser alterado:")
    while codigoProduto not in df.index:  # ["Codigo_Produto"].to_string():

        print("Código não encontrado.")
        codigoProduto = input("Insira o código do produto a ser alterado:")

    opcao = 0
    while opcao not in [1, 2, 3]:
        opcao = int(input(""" Insira uma das opções abaixo:
        1 - para alterar o nome do produto,
        2 - para alterar a categoria do produto,
        3 - para alterar o preço do produto."""))
        if opcao == 1:
            print(f"O antigo nome do produto é {df.loc[[codigoProduto], ['Nome_Produto']].values[0][0]}.")
            while True:
                try:
                    novoNomeProduto = input("Insira o novo nome para o produto:")
                    if novoNomeProduto.isdigit():
                        raise Exception
                    elif len(novoNomeProduto.replace(" ", "")) == 0:
                        raise Exception
                except:
                    print("Nome não permitido para produto.")
                else:
                    break
            df.loc[[codigoProduto], ['Nome_Produto']] = novoNomeProduto
            df.to_csv("Produto.csv", sep=";")
            print(f"O novo nome do produto é {df.loc[[codigoProduto], ['Nome_Produto']].values}.")

        elif opcao == 2:
            print(f"A antiga categoria do produto é {df.loc[[codigoProduto], ['Categoria_Produto']].values}0\n.")
            categoriaProduto = inputCategoria()
            df.loc[[codigoProduto], ['Categoria_Produto']] = categoriaProduto
            df.to_csv("Produto.csv", sep=";")
            print(f"A nova categoria do produto é {df.loc[[codigoProduto], ['Categoria_Produto']].values}.")
        elif opcao == 3:
            print(f"O antigo preço do produto é {df.loc[[codigoProduto], ['Preco']].values}.")
            while True:
                novoPrecoProduto = input("Insira o novo preço para o produto:")
                if novoPrecoProduto.replace(",", "").isdigit() and int(novoPrecoProduto).replace(",", "") > 0:
                    break
                else:
                    print("Preço de produto inválido ...")
            df.loc[[codigoProduto], ['Preco']] = novoPrecoProduto
            df.to_csv("Produto.csv", sep=";")
            print(f"O novo preço do produto é {df.loc[[codigoProduto], ['Preco']].values}.")
        else:
            print("Opção inexistente!")


def deletarProduto():
    df = pd.read_csv("../DataBase/Produto.csv", delimiter=";")
    df.set_index('Codigo_Produto', inplace=True)
    print(df)
    codigoProduto = input("Insira o código do produto a ser deletado:")
    while codigoProduto not in df.index:
        print("Código não encontrado.")
        codigoProduto = input("Insira o código do produto a ser deletado:")
    df.drop(codigoProduto, inplace=True)
    df.to_csv("Produto.csv", sep=";")
    print(f"Produto excluído! Código: {codigoProduto}")


def deletarCategoria():
    df = pd.read_csv("../DataBase/Categoria.csv", delimiter=";")
    print("CATEGORIAS DISPONÍVEIS:")
    print(df)
    while True:
        try:
            delCategoria = input("Insira o nome da categoria a ser deletada:")
            if delCategoria not in df.values:
                raise Exception
        except:
            print("A categoria não foi encontrada.")
        else:
            # MODIFICA O CSV DE CATEGORIAS
            df.replace(delCategoria, "None", inplace=True)
            df.to_csv("Categoria.csv", sep=";", index=False)

            # MODIFICA O CSV DE PRODUTO
            df2 = pd.read_csv("../DataBase/Produto.csv", delimiter=";")
            df2.set_index('Codigo_Produto', inplace=True)
            df2.Categoria_Produto.replace(delCategoria, "None", inplace=True)
            df2.to_csv("Produto.csv", sep=";")

            print(f"Categoria {delCategoria} substituída por 'None'")
            break
