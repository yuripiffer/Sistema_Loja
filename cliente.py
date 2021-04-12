import pandas as pd
import areaVendas


def cadastro_Cliente():
    print("\n Cadastro de Pessoas:")
    nome_Cliente = input("Nome: ")
    idade_Cliente = input("Idade: ")
    cpf_Cliente = input("CPF: ")

    if cpf_Cliente in str(pd.read_csv("Cliente.csv", delimiter=";", dtype=str)["CPF"]):
        print("\n CPF já registrado ...")
    else:
        with open("Cliente.csv", "a") as file:
            file.write(f"{cpf_Cliente};{nome_Cliente};{idade_Cliente}\n")
        print("\n Cadastro registrado !!")


def consulta_Cliente():
    print(pd.read_csv("Cliente.csv", delimiter=";", dtype=str))


def area_Vendas_Cliente():
    opcao = 0
    while True:
        opcao = input("\n Area de vendas:\n"
                      "1 -> Comprar como cliente (4% desc)\n"
                      "2 -> Comprar como desconhecido\n"
                      "3 -> Sair\n"
                      " Opção: ")

        if opcao == "1":
            logar_Cliente()
        elif opcao == "2":
            areaVendas.vender_Produtos()
            break
        elif opcao == "3":
            break


def logar_Cliente():
    cpf_Cliente = input("\n CPF do cliente: ")
    if cpf_Cliente in str(pd.read_csv("Cliente.csv", delimiter=";", dtype=str)["CPF"]):
        areaVendas.vender_Produtos()
    else:
        print("Cliente não cadastrado ...")
