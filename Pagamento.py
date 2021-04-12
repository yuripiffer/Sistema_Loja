import pandas as pd
from datetime import datetime


def pagamento(listaProduto):
    valorCompra = calcularListaProdutos(listaProduto)
    print("FINALIZAÇÃO DE COMPRA\n"
          f"Valor atual da compra: R${valorCompra}")
    opcao = "0"
    while opcao != "3":
        opcao = input("SISTEMA DE PAGAMENTO\n"
                      "Opções de pagamento:\n"
                      "\t1 -> Dinheiro\n"
                      "\t2 -> Cartão de débito\n"
                      "\t3 -> Sair\n")
        if opcao == "1":
            compraDinheiro(valorCompra)
            inserirHistoricoCompra(listaProduto)
        elif opcao == "2":
            compraCartao(valorCompra)
            inserirHistoricoCompra(listaProduto)
        elif opcao == "3":
            pass


def calcularListaProdutos(listaProduto):
    df = pd.read_csv("Produto.csv", delimiter=";")
    df.set_index('Codigo_Produto', inplace=True)
    valorCompra = 0
    for codigoProduto in listaProduto:
        valorUnidadeString = str(df.loc[[codigoProduto], ["Preco"]].values[0][0]).replace(',', '.')
        valorUnidade = float(valorUnidadeString)
        valorCompra += valorUnidade
    return valorCompra


def compraDinheiro(valorCompra):
    print("CÁLCULO DE TROCO:")
    print(f"Valor total da compra: R${valorCompra}")
    dinheiroCliente = float(input("Insira o valor entregue pelo cliente:"))
    troco = float(dinheiroCliente - valorCompra)
    print(f"Troco a ser entregue para o cliente: R$ {troco}\n")
    # COMPUTAR COMO COMPRA REALIZADA NO HISTÓRICO DE COMPRA


def compraCartao(valorCompra):
    df = pd.read_csv("DadosCartao.csv", delimiter=";")
    df.set_index('N_Cartao', inplace=True)

    while True:
        try:
            nCartao = int(input("Insira o número do cartão (4 dígitos):\n"))
            if nCartao not in df.index:
                raise Exception
            break  # NÃO É IF, NÃO TEM EXCEÇÃO...
        except:
            print("OPS! Número de cartão não encontrado ou número inserido incorretamente")

    while True:
        try:
            validadeCartao = int(input("Insira a data de validade do cartão (MM/AA, sem '/') :\n"))
            if validadeCartao != int(df.loc[[nCartao], ["Validade(mm/yy)"]].values):
                raise Exception
            break
        except:
            print("OPS! Validade de cartão errada ou número inserido incorretamente")

    while True:
        try:
            senhaCartao = int(input("Insira a senha do cartão (3 dígitos):\n"))
            if senhaCartao != int(df.loc[[nCartao], ["Senha"]].values):
                raise Exception
            break
        except:
            print("OPS! Senha do cartão errada ou número inserido incorretamente")

    saldo = int(df.loc[[nCartao], ["Saldo"]].values)
    if saldo < valorCompra:
        print("Saldo insuficiente.")
    else:
        novoSaldoCartao = saldo - valorCompra
        print("Compra realizada!\n"
              f"Novo saldo do cartão: R${novoSaldoCartao}\n")

        df.loc[[nCartao], ["Saldo"]] = novoSaldoCartao
        df.to_csv("DadosCartao.csv", sep=";")


def inserirHistoricoCompra(listaProduto):
    df = pd.read_csv("Produto.csv", delimiter=";")
    df.set_index('Codigo_Produto', inplace=True)
    dataCompra = datetime.now().strftime("%m/%d/%Y - %H:%M:%S")
    for codigoProduto in listaProduto:
        nomeProduto = df.loc[[codigoProduto], ["Nome_Produto"]].values[0][0]
        precoProduto = df.loc[[codigoProduto], ["Preco"]].values[0][0]
        with open("Historico_compras.csv", "a") as f:
            input_dado = f"{dataCompra};{codigoProduto};{nomeProduto};{precoProduto}\n"
            f.write(input_dado)


def consultarHistoricoCompra():
    print(pd.read_csv("Historico_compras.csv", delimiter=";"))

