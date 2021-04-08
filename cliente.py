import pandas as pd


def cadastro_Cliente():

    print("\n Cadastro de Pessoas:")
    nome_Cliente = input("Nome: ")
    idade_Cliente = input("Idade: ")
    cpf_Cliente = input("CPF: ")

    if cpf_Cliente in str(pd.read_csv("Cliente.csv", delimiter=";", dtype=str)["CPF"]):
        print("\n CPF já cadastrado ...")
    else:
        with open("Cliente.csv", "a") as file:
            file.write(f"{cpf_Cliente};{nome_Cliente};{idade_Cliente}\n")
        print("\n Cadastro registrado !!")


def consulta_Cliente():
    print(pd.read_csv("Cliente.csv", delimiter=";", dtype=str))

