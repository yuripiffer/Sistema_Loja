import pandas as pd
from Menu import menuVendas
import cpf_tools


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
        cpf_Cliente = (input("CPF: (sem pontos ou traço")).replace(".", "").replace("-", "")
        if not cpf_tools.cpf_str_validation(cpf_Cliente):
            print("CPF inválido ...")
            cpf_Cliente = ""

    if cpf_Cliente in str(pd.read_csv("../DataBase/Cliente.csv", delimiter=";", dtype=str)["CPF"]):
        print("\n CPF já registrado ...")
    else:
        with open("../DataBase/Cliente.csv", "a") as file:
            file.write(f"{cpf_Cliente};{nome_Cliente};{idade_Cliente}\n")
        print("\n Cadastro registrado !!")


def consulta_Cliente():
    print(pd.read_csv("../DataBase/Cliente.csv", delimiter=";", dtype=str))


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
            menuVendas.vender_Produtos()
            break
        elif opcao == "3":
            break


def logar_Cliente():
    while True:
        try:
            cpf_Cliente = (input("\n Insira o CPF do cliente: (sem pontos e traço)")).replace(".", "").replace("-", "")
            if len(cpf_Cliente) != 11:
                raise Exception
            elif cpf_Cliente not in str(pd.read_csv("../DataBase/Cliente.csv", delimiter=";", dtype=str)["CPF"]):
                raise Exception
        except:
            print("OPS! Problemas com a entrada de dados do CPF.")
        else:
            nome =
            # DAR BEM-VINDO AO USUÁRIO
            menuVendas.vender_Produtos()
