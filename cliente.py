import pandas as pd
import areaVendas
import cpf_tools
import string

def cadastro_Cliente():
    nome_Cliente = ""
    idade_Cliente = ""
    cpf_Cliente = ""

    print("\n Cadastro de Pessoas:")
    while nome_Cliente == "":
        nome_Cliente = input("Nome: ")
        if not nome_Cliente.replace(" ", "").isalpha() or len(nome_Cliente) < 5:
            print("Nome inválido ... ")
            nome_Cliente = ""
    while idade_Cliente == "":
        idade_Cliente = input("Idade: ")
        if not idade_Cliente.isdigit() or int(idade_Cliente) > 150 or int(idade_Cliente) < 18:
            print("Idade inválida ...")
            idade_Cliente = ""
    while cpf_Cliente == "":
        cpf_Cliente = input("CPF: ")
        if not cpf_tools.cpf_str_validation(cpf_Cliente):
            print("CPF inválido ...")
            cpf_Cliente = ""

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
                      "1 -> Comprar como cliente\n"
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
